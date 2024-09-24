# Find Left-Behind Folders

This C# console application helps identify and fix left-behind folders in the `rules` directory. 
It moves the files from the old folders to the new folders according to the `redirects` list specified in the `rule.md` files and then removes the old folders.

The script was created to fix https://github.com/SSWConsulting/SSW.Rules.Content/issues/5292