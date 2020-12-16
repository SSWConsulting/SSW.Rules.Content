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

    let file = fs.readFileSync('../../../../../files.json');
    let changedFiles = JSON.parse(file); 
    console.log(`processing ${changedFiles.length} changed files`);

    for (const changedFilePath of changedFiles) {
        if (!changedFilePath.startsWith('rules')) continue;

        console.log('changed path: ',changedFilePath);
        let historyRecord  = historyData.find(f => f.file == changedFilePath);
        console.log('history record: ',historyRecord);

    }

} catch (error) {
    core.setFailed(error.message);
}

