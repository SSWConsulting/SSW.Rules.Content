---
type: rule
seoDescription: Learn how to change the date of an existing commit
archivedreason: 
title: Do you know how to change the date of an existing commit?
guid: f29b94c2-14be-4900-8734-924c9a576f4e
uri: change-date-of-existing-commit
created: 2024-07-29T11:06:33.0000000Z
authors:
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- clean-git-history
redirects: []

---

Updating commit information can be essential for maintaining accurate project history or correcting errors. Whether you need to change a commit date for clarity, compliance, or other reasons, you have a couple of methods at your disposal.

This rule outlines how to change the date of an existing commit using both a manual CLI approach and an automated script.

<!--endintro-->

## Method 1 – Use CLI

1. Checkout to the branch containing the commit

```bash
git checkout -b {{ BRANCH NAME }} origin/{{ BRANCH NAME }}
```

2. Run git log to get the last commit hash
  
```bash
git log
```

3. Do an interactive rebase for the parent of the last commit
  
```bash
git rebase -i {{ COMMIT HASH }}^
```

4. This opens vi editor:

    1. Press "I" key to enter interactive mode,
    2. Change "pick" to "edit",
    3. Press "escape" to exit interactive mode,
    4. Type ":wq" to save and exit

5. Change the commit date
  
``` bash
GIT_COMMITTER_DATE="{{ NEW DATE IN  'YYYY-MM-DD HH:MM:SS' FORMAT }}" GIT_AUTHOR_DATE="{{ NEW DATE IN  'YYYY-MM-DD HH:MM:SS' FORMAT }}" git commit --amend --no-edit
```

6. Finish the rebase

```bash
git rebase --continue
```

7. Force push to origin

```bash
git push origin {{ BRANCH NAME }} --force
```

## Method 2 (recommended) – Use a script

If the date change is to be applied on several branches, it is preferable to automate the process with a script.

```bash
BRANCH=$1
DATE=$2
if [ -z "$BRANCH" ] || [ -z "$DATE" ]; then
   echo "Usage: $0 {{ BRANCH NAME }} {{ NEW DATE IN  'YYYY-MM-DD HH:MM:SS' FORMAT }}"
   exit 1
fi
git checkout -b "$BRANCH" "origin/$BRANCH"
LAST_COMMIT_HASH=$(git log -n 1 --pretty=format:"%H")  
git rebase -i "$LAST_COMMIT_HASH^"
GIT_COMMITTER_DATE="$DATE" GIT_AUTHOR_DATE="$DATE" git commit --amend --no-edit
git rebase --continue
git push origin "$BRANCH" --force
git checkout main
```

The script can be actioned with the following command:

```bash
./change_history.sh "{{ LOCAL PATH }}" "{{ NEW DATE IN  'YYYY-MM-DD HH:MM:SS' FORMAT }}"
```
