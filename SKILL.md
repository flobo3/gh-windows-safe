---
name: gh-windows-safe
description: Safe wrapper for GitHub CLI (gh) on Windows. Automatically handles multi-line text by writing it to a temporary file and using --body-file, preventing CMD truncation and path traversal errors.
metadata: {"nanobot":{"emoji":"🛡️"}}
---

# gh-windows-safe

A safe wrapper for GitHub CLI (`gh`) on Windows. 

When you need to create or edit an issue, pull request, or comment with multi-line text, the standard `gh` command on Windows CMD often truncates the text after the first newline or triggers path traversal protections if you use the `--body` flag.

This skill provides a safe Python wrapper that automatically writes your multi-line text to a temporary file and calls `gh` with the `--body-file` flag.

## Usage

### Create an Issue Comment
```bash
python ~/.nanobot/workspace/skills/gh-windows-safe/gh_safe.py issue comment <issue_number> --repo <owner/repo> --body "Your multi-line\ntext here"
```

### Create a Pull Request
```bash
python ~/.nanobot/workspace/skills/gh-windows-safe/gh_safe.py pr create --repo <owner/repo> --title "PR Title" --body "Your multi-line\nPR description" --head <branch>
```

### Edit a Pull Request
```bash
python ~/.nanobot/workspace/skills/gh-windows-safe/gh_safe.py pr edit <pr_number> --repo <owner/repo> --body "Updated multi-line\nPR description"
```

## How it works
The script intercepts the `--body` argument, writes its content to a temporary `.txt` file in the system temp directory, replaces `--body` with `--body-file <temp_file>`, executes the `gh` command, and then cleans up the temporary file. All other arguments are passed directly to `gh`.