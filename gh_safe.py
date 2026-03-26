import sys
import os
import subprocess
import tempfile

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python gh_safe.py <gh_command> [args...]")
        sys.exit(1)

    gh_args = []
    body_content = None
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--body":
            if i + 1 < len(args):
                body_content = args[i+1]
                i += 2
            else:
                print("Error: --body requires an argument")
                sys.exit(1)
        else:
            gh_args.append(arg)
            i += 1

    temp_file_path = None
    if body_content is not None:
        # Create a temporary file in the system temp directory
        temp_dir = tempfile.gettempdir()
        temp_file_path = os.path.join(temp_dir, "gh_safe_temp_body.txt")
        
        # Handle escaped newlines from command line
        body_content = body_content.replace("\\n", "\n")
        
        with open(temp_file_path, "w", encoding="utf-8") as f:
            f.write(body_content)
            
        gh_args.extend(["--body-file", temp_file_path])

    command = ["gh"] + gh_args
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"Error executing gh: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except Exception as e:
                print(f"Warning: Could not remove temporary file {temp_file_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()