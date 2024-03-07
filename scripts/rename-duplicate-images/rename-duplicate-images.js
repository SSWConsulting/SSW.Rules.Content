const fs = require("fs");
const path = require("path");

function checkDuplicateImages(directory) {
  const duplicateImages = {};
  let totalModifiedFiles = 0;

  fs.readdirSync(directory).forEach((file) => {
    const filePath = path.join(directory, file);
    if (fs.statSync(filePath).isDirectory()) {
      fs.readdirSync(filePath).forEach((subfile) => {
        const subfilePath = path.join(filePath, subfile);
        if (
          fs.statSync(subfilePath).isFile() &&
          subfile.match(/\.(png|jpg|jpeg|gif)$/)
        ) {
          if (subfile in duplicateImages) {
            duplicateImages[subfile].push(subfilePath);
          } else {
            duplicateImages[subfile] = [subfilePath];
          }
        }
      });
    }
  });

  // Rename duplicate images
  Object.keys(duplicateImages).forEach((fileName) => {
    const paths = duplicateImages[fileName];
    if (paths.length > 1) {
      const newName = generateNewName(fileName);
      //   paths.forEach((path, index) => {
      //     const newPath = path.replace(fileName, newName);
      //     fs.renameSync(path, newPath);
      //     paths[index] = newPath;
      //     totalModifiedFiles++;
      //   });
      const firstPath = paths.shift();
      const newPath = firstPath.replace(fileName, newName);
      fs.renameSync(firstPath, newPath);
      totalModifiedFiles++;
      // if (fs.existsSync(path.dirname(paths[0]) + "/rule.md")) {
      //   modifyRuleMd(path.dirname(paths[0]) + "/rule.md", fileName, newName);
      // }
    }
  });

  console.log(`Total modified files: ${totalModifiedFiles}`);
}

function generateNewName(fileName) {
  const nameWithoutExtension = path.parse(fileName).name;
  const extension = path.parse(fileName).ext;
  const timestamp = new Date().getTime();
  return `${nameWithoutExtension}_${timestamp}${extension}`;
  //   return `${nameWithoutExtension}_${randomId}${extension}`;
}

function modifyRuleMd(ruleMdPath, oldImageName, newImageName) {
  const ruleMdContent = fs.readFileSync(ruleMdPath, "utf-8");
  const newContent = ruleMdContent.replace(
    new RegExp(oldImageName, "g"),
    newImageName
  );
  fs.writeFileSync(ruleMdPath, newContent, "utf-8");
}

const directory = "../../rules";

checkDuplicateImages(directory);
