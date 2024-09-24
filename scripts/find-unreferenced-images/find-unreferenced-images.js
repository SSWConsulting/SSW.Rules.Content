const fs = require('fs');
const path = require('path');
const marked = require('marked');
const core = require('@actions/core');

function findImagesInMarkdown(file) {
    const nodeList = []
    const markdown = fs.readFileSync(file, "utf8");

    if (!markdown) return

    const walkTokens = (token) => {
        if (token.type === "image") {
            nodeList.push(token.href)
        }
    };

    marked.use({ walkTokens });
    marked.parse(markdown, { mangle: false, headerIds: false });

    return [...new Set(nodeList)];
}

function traverseEverything(directory) {
    const images = {};

    recTraverseDirectory(directory, images);

    return images;
}

function traverseDirectories(directories) {
    const images = {};

    directories.forEach(directory => {
        const subdirectoryImages = recTraverseDirectory(directory, images);
        const intersection = subdirectoryImages.folderImages.filter(x => !subdirectoryImages.markdownImages.includes(x));

        if (intersection.length > 0) {
            images[directory.replaceAll("../", "").replaceAll("rules/", "")] = intersection;
        }
    });

    return images;
}

function recTraverseDirectory(directory, images) {
    const markdownImages = [];
    const folderImages = [];

    if (!fs.existsSync(directory)) {
        return { markdownImages, folderImages };
    }

    const files = fs.readdirSync(directory);

    for (const file of files) {
        const filePath = path.join(directory, file);
        const stats = fs.statSync(filePath);

        if (stats.isDirectory()) {
            const subdirectoryImages = recTraverseDirectory(filePath, images);
            const intersection = subdirectoryImages.folderImages.filter(x => !subdirectoryImages.markdownImages.includes(x));

            if (intersection.length > 0) {
                images[filePath.replaceAll("../", "").replaceAll("rules/", "")] = intersection;
            }
        } else if (file.toLowerCase() === 'rule.md') {
            const images = findImagesInMarkdown(filePath);
            markdownImages.push(...images);
        } else if (stats.isFile() && /\.(png|jpg|jpeg|gif|svg|pdf)$/i.test(file)) {
            folderImages.push(file);
        }
    }

    return { markdownImages, folderImages };
}

async function main() {
    const eventType = process.env.GITHUB_EVENT_NAME;
    const branch = process.env.GITHUB_HEAD_REF || "main";
    const repo = process.env.GITHUB_REPOSITORY;
    let images;

    if (eventType === "pull_request") {
        if (process.argv[2] && process.argv[2].length > 0) {
            const folders = process.argv[2]
                .split(",")
                .filter(file => file.slice(0, 5) == "rules")
                .map(folder => `../../${folder.split("/").slice(0, -1).join("/")}`);

            images = traverseDirectories(folders);
        }
    } else if (eventType === "workflow_dispatch") {
        images = traverseEverything("../../rules/");
    }
    
    if (images === undefined || images === null || Object.keys(images).length === 0) {
        await core.summary.addHeading("No unreferenced images found").addSeparator().write();
        return;
    }
    await core.summary.addHeading(`Found ${Object.keys(images).length} unreferenced images`).addSeparator().write();

    for (const [idx, rule] of Object.keys(images).entries()) {
        await core.summary.addLink(`${idx + 1}. ${rule}`, `https://github.com/${repo}/tree/${branch}/rules/${rule}`).addList(images[rule]).write();
    }
}

main();
