# Microsoft Creator ID Script

Automatically adds Microsoft Creator IDs to URLs in markdown files to track referrals to Microsoft documentation and learning resources.

## What It Does

* Finds Microsoft URLs in markdown files (docs.microsoft.com, learn.microsoft.com, etc.)
* Adds appropriate Creator IDs based on content category (Azure, .NET, M365, etc.)
* Preserves existing URLs that already have Creator IDs

## How to Run

```bash
# Test first (see what would change)
python3 add_creator_ids.py --creator-id MVP-{{YOUR_CREATOR_ID}} --dry-run

# Apply changes to all markdown files
python3 add_creator_ids.py --creator-id MVP-{{YOUR_CREATOR_ID}}
```

### Example

**Before:**

```markdown
Check out the [Azure documentation](https://docs.microsoft.com/en-us/azure/) for more info.
```

**After:**

```markdown
Check out the [Azure documentation](https://docs.microsoft.com/en-us/azure/?WT.mc_id=AZ-MVP-33518) for more info.
```
