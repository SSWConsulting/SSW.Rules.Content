#!/usr/bin/env node

'use strict'

const fs = require('fs');
const core = require('@actions/core');
const github = require('@actions/github');

try {

    let historyFile = fs.readFileSync('../../history.json');
    let historyData = JSON.parse(historyFile);
    console.log(`got ${historyData.length} history records`);

    // history files are written above the working folders
    // current folder: /home/runner/work/SSW.Rules.Content/SSW.Rules.Content/scripts/update-history
    // files.json home folder: /home/runner
    let file = fs.readFileSync('../../../../../files.json');
    let changedFiles = JSON.parse(file); 
    console.log(`processing ${changedFiles.length} changed files`);

    for (const changedFilePath of changedFiles) {
        if (!changedFilePath.startsWith('rules')) continue;

        console.log('changed path: ', changedFilePath);
        let historyRecord  = historyData.find(f => f.file == changedFilePath);
        console.log('history record before: ', historyRecord);

        if (historyRecord) {
            historyRecord.lastUpdated = new Date().toISOString();
            historyRecord.lastUpdatedBy = process.env.GIT_COMMIT_AUTHOR_NAME;
            historyRecord.lastUpdatedByEmail = process.env.GIT_COMMIT_AUTHOR_EMAIL
        } else {
            historyRecord = {
                file: changedFilePath,
                created: new Date().toISOString(),
                createdBy: process.env.GIT_COMMIT_AUTHOR_NAME,
                createdByEmail: process.env.GIT_COMMIT_AUTHOR_EMAIL,
                lastUpdated: new Date().toISOString(),
                lastUpdatedBy: process.env.GIT_COMMIT_AUTHOR_NAME,
                lastUpdatedByEmail: process.env.GIT_COMMIT_AUTHOR_EMAIL
            };
        }
        console.log('history record after: ', historyRecord);
    }

} catch (error) {
    core.setFailed(error.message);
}

