const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const marked = require('marked');
const core = require('@actions/core');

const RULES_ROOT = "../../public/uploads/rules";

function normalizeImageReference(reference) {
    if (!reference) {
        return null;
    }

    const cleanedReference = reference.split("?")[0].split("#")[0];
    const fileName = path.basename(cleanedReference);

    return fileName || null;
}

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

    const imageEmbedRegex = /<imageEmbed\b[^>]*\bsrc=(?:"([^"]+)"|'([^']+)')/g;
    let match;

    while ((match = imageEmbedRegex.exec(markdown)) !== null) {
        nodeList.push(match[1] || match[2]);
    }

    return [...new Set(nodeList.map(normalizeImageReference).filter(Boolean))];
}

function getChangedRuleDirectories() {
    const mergeBase = execSync("git merge-base origin/main HEAD", {
        encoding: "utf8"
    }).trim();
    const diffOutput = execSync(`git diff --name-only ${mergeBase} HEAD`, {
        encoding: "utf8"
    });

    return [...new Set(
        diffOutput
            .split(/\r?\n/)
            .filter(file => file.startsWith("public/uploads/rules/"))
            .map(file => path.posix.dirname(file))
            .filter(directory => directory !== "public/uploads/rules")
            .map(directory => `../../${directory}`)
    )];
}

function getRuleKey(directory) {
    return directory.replace(`${RULES_ROOT}/`, "");
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
            images[getRuleKey(directory)] = intersection;
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
                images[getRuleKey(filePath)] = intersection;
            }
        } else if (["rule.md", "rule.mdx"].includes(file.toLowerCase())) {
            const images = findImagesInMarkdown(filePath);
            markdownImages.push(...images);
        } else if (stats.isFile() && /\.(png|jpg|jpeg|gif|svg|pdf|webp)$/i.test(file)) {
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
        const folders = getChangedRuleDirectories();
        if (folders.length > 0) {
            images = traverseDirectories(folders);
        }
    } else if (eventType === "workflow_dispatch") {
        images = traverseEverything(RULES_ROOT);
    }
    
    if (images === undefined || images === null || Object.keys(images).length === 0) {
        await core.summary.addHeading("No unreferenced images found").addSeparator().write();
        return;
    }
    await core.summary.addHeading(`Found ${Object.keys(images).length} unreferenced images`).addSeparator().write();

    for (const [idx, rule] of Object.keys(images).entries()) {
        await core.summary.addLink(`${idx + 1}. ${rule}`, `https://github.com/${repo}/tree/${branch}/public/uploads/rules/${rule}`).addList(images[rule]).write();
    }
}

main();
