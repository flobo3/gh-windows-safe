# gh-windows-safe 🛡️

A safe wrapper for GitHub CLI (`gh`) on Windows to prevent multi-line text truncation.

## The Problem

If you use the standard GitHub CLI (`gh`) on Windows Command Prompt (CMD) to create or edit issues, pull requests, or comments, you might run into a frustrating bug: **CMD truncates multi-line strings passed to the `--body` flag after the first newline (`\n`).** 

Additionally, some AI agents and sandboxes might block commands containing certain special characters due to path traversal protections.

## The Solution

`gh-windows-safe` is a lightweight Python wrapper that solves this by:
1. Intercepting the `--body` argument.
2. Writing your multi-line text into a temporary file in the system's temp directory.
3. Replacing `--body` with `--body-file <temp_file>` before calling the actual `gh` CLI.
4. Automatically cleaning up the temporary file after execution.

This guarantees that all your paragraphs, lists, and formatting are preserved perfectly!

## Usage

Use it exactly like you would use `gh`, just call the Python script instead:

```bash
# Create an Issue Comment
python gh_safe.py issue comment 123 --repo owner/repo --body "Line 1\nLine 2\nLine 3"

# Create a Pull Request
python gh_safe.py pr create --repo owner/repo --title "Fix bug" --body "Description:\n- Item 1\n- Item 2" --head feature-branch
```

All other arguments are passed directly to the underlying `gh` command.