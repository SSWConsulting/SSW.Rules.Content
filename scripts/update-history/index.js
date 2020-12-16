#!/usr/bin/env node

'use strict'

const fs = require('fs');
const core = require('@actions/core');
const github = require('@actions/github');

try {
    let historyFile = fs.readFileSync('../../history.json');
    let historyData = JSON.parse(historyFile);

    let addedFile = fs.readFileSync('../../files_added.json');
    let addedData = JSON.parse(addedFile);

    let modifiedFile = fs.readFileSync('../../files_modified.json');
    let modifiedData = JSON.parse(modifiedFile);

    let file = fs.readFileSync('../../files.json');
    let data = JSON.parse(file);

    console.log(`got ${historyData.length} history records`);
    console.log(`got ${addedData.length} added files`);
    console.log(`got ${modifiedData.length} modified files`);
    console.log(`got ${data.length} from files.json`);

} catch (error) {
    core.setFailed(error.message);
}

