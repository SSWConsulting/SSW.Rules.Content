const fs = require('fs');
const path = require('path');
const marked = require('marked');
const core = require('@actions/core');

function findImagesInMarkdown(file) {
    const node_list = []
    const markdown = fs.readFileSync(file, "utf8");

    if (!markdown) return

    const walkTokens = (token) => {
        if (token.type === "image") {
            node_list.push(token.href)
        }
    };

    marked.use({ walkTokens });
    marked.parse(markdown, { mangle: false, headerIds: false });

    return [...new Set(node_list)];
}

function traverse_everything(directory) {
    const images = {};

    rec_traverse_directory(directory, images);

    return images;
}

function traverse_directories(directories) {
    const images = {};

    directories.forEach(directory => {
        const subdirectory_images = rec_traverse_directory(directory, images);
        const intersection = subdirectory_images.folder_images.filter(x => !subdirectory_images.markdown_images.includes(x));

        if (intersection.length > 0) {
            images[directory.replaceAll("../", "").replaceAll("rules/", "")] = intersection;
        }
    });

    return images;
}

function rec_traverse_directory(directory, images) {
    const files = fs.readdirSync(directory);
    const markdown_images = [];
    const folder_images = [];

    for (const file of files) {
        const file_path = path.join(directory, file);
        const stats = fs.statSync(file_path);

        if (stats.isDirectory()) {
            const subdirectory_images = rec_traverse_directory(file_path, images);
            const intersection = subdirectory_images.folder_images.filter(x => !subdirectory_images.markdown_images.includes(x));

            if (intersection.length > 0) {
                images[file_path.replaceAll("../", "").replaceAll("rules/", "")] = intersection;
            }
        } else if (file.toLowerCase() === 'rule.md') {
            const images = findImagesInMarkdown(file_path);
            markdown_images.push(...images);
        } else if (stats.isFile() && /\.(png|jpg|jpeg|gif|svg)$/i.test(file)) {
            folder_images.push(file);
        }
    }

    return { markdown_images, folder_images };
}

async function main() {
    const event_type = process.env.GITHUB_EVENT_NAME;
    const branch = process.env.GITHUB_HEAD_REF || "main";
    let images;

    if (event_type === "pull_request") {
        const folders = process.argv[2]
            .split(",")
            .filter(file => file.slice(0, 5) == "rules")
            .map(folder => `../../${folder.split("/").slice(0, -1).join("/")}`);

        images = traverse_directories(folders);
    } else if (event_type === "workflow_dispatch") {
        images = traverse_everything("../../rules/");
    }

    await core.summary.addHeading(`Found ${Object.keys(images).length} unreferenced images`).addSeparator().write();

    for (const [idx, rule] of Object.keys(images).entries()) {
        await core.summary.addLink(`${idx + 1}. ${rule}`, `https://github.com/BrookJeynes/SSW.Rules.Content/tree/${branch}/rules/${rule}`).addList(images[rule]).write();
    }
}

main();
