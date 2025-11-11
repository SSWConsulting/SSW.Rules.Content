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

function checkForOrphanFolders(rulesDirectory) {
    const orphans = {};

    if (!fs.existsSync(rulesDirectory)) {
        return orphans;
    }

    const folders = fs.readdirSync(rulesDirectory);

    for (const folder of folders) {
        const folderPath = path.join(rulesDirectory, folder);
        const stats = fs.statSync(folderPath);

        if (stats.isDirectory()) {
            const ruleMdPath = path.join(folderPath, 'rule.md');
            const hasRuleMd = fs.existsSync(ruleMdPath);

            if (!hasRuleMd) {
                // This folder has no rule.md - check if it has any files
                const files = fs.readdirSync(folderPath);
                const imageFiles = files.filter(file => {
                    const filePath = path.join(folderPath, file);
                    const fileStats = fs.statSync(filePath);
                    return fileStats.isFile() && /\.(png|jpg|jpeg|gif|svg|pdf|xlsx?)$/i.test(file);
                });

                if (imageFiles.length > 0) {
                    // This is an orphan folder - has files but no rule.md
                    orphans[folderPath.replaceAll("../", "").replaceAll("rules/", "")] = imageFiles;
                }
            }
        }
    }

    return orphans;
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
    let hasRuleMd = false;

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
            hasRuleMd = true;
            const images = findImagesInMarkdown(filePath);
            markdownImages.push(...images);
        } else if (stats.isFile() && /\.(png|jpg|jpeg|gif|svg|pdf)$/i.test(file)) {
            folderImages.push(file);
        }
    }

    // Check if this directory has images/files but no rule.md (orphan folder)
    // This is a critical issue as it indicates a leftover folder from a rename
    if (!hasRuleMd && folderImages.length > 0) {
        images[directory.replaceAll("../", "").replaceAll("rules/", "")] = folderImages;
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

            // Check changed folders for unreferenced images
            images = traverseDirectories(folders);
        } else {
            // No changed files, but still need to check for orphan folders
            images = {};
        }

        // Always check for orphan folders (folders with files but no rule.md) in the entire rules directory
        // This catches leftover folders from renames that aren't in the PR diff
        const orphanFolders = checkForOrphanFolders("../../rules/");
        Object.assign(images, orphanFolders);
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

    // Fail the workflow when unreferenced images or orphan folders are found
    core.setFailed(`Found ${Object.keys(images).length} folders with unreferenced images or orphan folders`);
}

main();
