#Step 0: Prep the Repo for git log
git commit-graph write --reachable --changed-paths

$startCommitHash = '9f84a60'
$endCommitHash = 'HEAD'
$ShouldGenerateHistoryString = $true
# Create a new boolean variable from the string input
$IsHistoryGenerationEnabled = [string]::Equals($ShouldGenerateHistoryString, "true", [System.StringComparison]::OrdinalIgnoreCase)

$filesProcessed = @{}
$historyFileArray = @()

#Step 2: Get commits within range 
$listOfCommits = git log --pretty="<HISTORY_ENTRY>%n%h%n%ad%n%aN%n%ae%n<FILES_CHANGED>" --name-status --date=iso-strict $startCommitHash^..$endCommitHash origin/main --
$historyChangeEntry = $listOfCommits -join "<LINE>"
$historyArray = $historyChangeEntry -split "<HISTORY_ENTRY>"

$commitSyncHash = "";
$rulesContentFolder = "./"

$historyArray | Foreach-Object {
    $historyEntry = $_ -split "<FILES_CHANGED>"
    $userDetails = $historyEntry[0] -split "<LINE>"
    $fileArray = $historyEntry[1] -split "<LINE>"

    if($commitSyncHash -eq "" -and $userDetails[1].Length -gt 5) {
        $commitSyncHash = $userDetails[1]
    }

    if ($IsHistoryGenerationEnabled) {
        Write-Output "Processing commit $userDetails[1]"
        $lastUpdated = $userDetails[2]
        $lastUpdatedBy = $userDetails[3]
        $lastUpdatedByEmail = $userDetails[4]
        
        $fileArray | Where-Object {$_ -Match "^*.md" } | Foreach-Object {
            $fileStatusLine = $_.Trim()
            $fileStatus = $fileStatusLine.Substring(0, 1) # Get the first character: M (modified), A (added), D (deleted), R (renamed)
            $filePaths = $fileStatusLine.Substring(1).Trim() -split "\s+" # For renamed files, this line will have 3 parts: {{random_number old_path new_path}}
            $filePath = ""
            $oldFilePath = ""

            if ($fileStatus -eq 'R') {
                $oldFilePath = $filePaths[1].Trim()
                $filePath = $filePaths[2].Trim()
            } else {
                $filePath = $filePaths[0].Trim()
            }

            Write-Output "file status: $fileStatus | file: $filePath | old file: $oldFilePath"

            if ($filesProcessed.ContainsKey($filePath) -and $fileStatus -eq 'R') {
                $historyFileArray | ForEach-Object {
                    if ($_.file -eq $filePath) {
                        $_.oldFile = $oldFilePath
                    }
                }
            }

            if(!$filesProcessed.ContainsKey($filePath) -and $fileStatus -ne 'D')
            {
                try {
                    $fullPath = Join-Path $rulesContentFolder $filePath
                    # We want to keep the original author of file for created record if file is renamed
                    if ($fileStatus -eq 'R') {
                        $createdRecord = git log --diff-filter=A --reverse --pretty="%ad<LINE>%aN<LINE>%ae<LINE>" --date=iso-strict -- $oldFilePath
                    } else {
                        $createdRecord = git log --diff-filter=A --reverse --pretty="%ad<LINE>%aN<LINE>%ae<LINE>" --date=iso-strict -- $filePath
                    }
                    $createdDetails = $createdRecord -split "<LINE>"
    
                    # Read and parse Markdown file to set title, uri, and archived status
                    $utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $false
                    $streamReader = New-Object System.IO.StreamReader -Arg $fullPath, $utf8NoBomEncoding
                    $content = $streamReader.ReadToEnd()
                    $streamReader.Close()
    
                    $lines = $content -split "`n"
                    $isArchived = $false

                    $titleLine = $lines | Where-Object { $_.StartsWith('title:') }
                    $title = if ($titleLine) { $titleLine.Substring(6).Trim() } else { "" }
                    
                    $uriLine = $lines | Where-Object { $_.Trim().StartsWith('uri:') }
                    $uri = if ($uriLine) { $uriLine.Substring(4).Trim() } else { "" }
    
                    $archivedReasonLine = $lines | Where-Object { $_.Replace(' ', '').StartsWith('archivedreason:') }
                    if ($archivedReasonLine) {
                        $archivedReason = $archivedReasonLine.Trim().Substring(15).Trim()
                        $isArchived = $archivedReason -ne 'null' -and $archivedReason -ne ''
                    }

                    $filesProcessed.Add($filePath, 0)

                    $historyFileArray += @{
                        file = $filePath
                        oldFile = $oldFilePath
                        title = $title
                        uri = $uri
                        isArchived = $isArchived
                        lastUpdated = $lastUpdated
                        lastUpdatedBy = $lastUpdatedBy
                        lastUpdatedByEmail = $lastUpdatedByEmail
                        created = if ($createdDetails[0] -ne $null) { $createdDetails[0] } else { $lastUpdated }
                        createdBy = if ($createdDetails[1] -ne $null) { $createdDetails[1] } else { $lastUpdatedBy }
                        createdByEmail = if ($createdDetails[2] -ne $null) { $createdDetails[2] } else { $lastUpdatedByEmail }
                    }

                    Write-Output "Processed file: $filePath"
                }
                catch {
                    Write-Output "Error processing file: $filePath"
                }
            }
        }
    }
}

Write-Output $historyFileArray

# if ($IsHistoryGenerationEnabled) {
#     #Step 3: UpdateRuleHistory - Send History Patch to AzureFunction
#     $historyFileContents = ConvertTo-Json $historyFileArray
#     $Uri = $AzFunctionBaseUrl + '/api/UpdateRuleHistory'
#     $Headers = @{'x-functions-key' = $UpdateRuleHistoryKey}
#     $Response = Invoke-WebRequest -Uri $Uri -Method Post -Body $historyFileContents -Headers $Headers -ContentType 'application/json; charset=utf-8'
# }

# if(![string]::IsNullOrWhiteSpace($commitSyncHash))
# {
#     #Step 4: UpdateHistorySyncCommitHash - Update Commit Hash with AzureFunction
#     $Uri = $AzFunctionBaseUrl + '/api/UpdateHistorySyncCommitHash'
#     $Headers = @{'x-functions-key' = $UpdateHistorySyncCommitHashKey}
#     $Body = @{
#         commitHash  = $commitSyncHash
#     }
#     $Result = Invoke-WebRequest -Uri $Uri -Method Post -Body $Body -Headers $Headers
# }

if ($IsHistoryGenerationEnabled) {
    Write-Output $historyFileContents
}

Write-Output $commitSyncHash
