#!/usr/bin/env node

'use strict'

const fs = require('fs');
const core = require('@actions/core');
const github = require('@actions/github');

try {

    // hgisotry files are written one level aboce the checked out work folder 

    let historyFile = fs.readFileSync('../../history.json');
    let historyData = JSON.parse(historyFile);
    console.log(`got ${historyData.length} history records`);

    let addedFile = fs.readFileSync('../../../files_added.json');
    let addedData = JSON.parse(addedFile);
    console.log(`got ${addedData.length} added files`);

    let modifiedFile = fs.readFileSync('../../../files_modified.json');
    let modifiedData = JSON.parse(modifiedFile);
    console.log(`got ${modifiedData.length} modified files`);

    let file = fs.readFileSync('../../../files.json');
    let data = JSON.parse(file);

 
    console.log(`got ${data.length} from files.json`);

} catch (error) {
    core.setFailed(error.message);
}

