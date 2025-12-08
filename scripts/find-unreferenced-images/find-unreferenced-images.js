const fs = require('fs');
const path = require('path');
const core = require('@actions/core');
const { unified } = require('unified');
const remarkParse = require('remark-parse').default;
const remarkMdx = require('remark-mdx').default; 
const { visit } = require('unist-util-visit');

function findImagesInMarkdown(file) {
  const code = fs.readFileSync(file, 'utf8');
  if (!code) return [];

  const tree = unified().use(remarkParse).use(remarkMdx).parse(code);
  const out = new Set();

  visit(tree, 'mdxJsxFlowElement', (node) => {
    if (node.name === 'imageEmbed') {
      const srcAttr = node.attributes.find(a => a.type === 'mdxJsxAttribute' && a.name === 'src');
      if (srcAttr && typeof srcAttr.value === 'string') {
        out.add(path.basename(srcAttr.value));
      }
    }
  });

  return [...out];
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
            images[directory.replaceAll("../", "").replaceAll("public/uploads/rules/", "")] = intersection;
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
        } else if (file.toLowerCase() === 'rule.mdx') {
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
                .filter(file => file.slice(0, 5) == "public/uploads/rules")
                .map(folder => `../../${folder.split("/").slice(0, -1).join("/")}`);

            images = traverseDirectories(folders);
        }
    } else if (eventType === "workflow_dispatch") {
        images = traverseEverything("../../public/uploads/rules/");
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
