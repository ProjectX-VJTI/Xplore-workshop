import pathlib
import subprocess
import shutil
import sys

def setup_solutions():
    # 1. Locate the file with Pathlib
    current_file = pathlib.Path(__file__).resolve()
    current_dir = current_file.parent

    # 2. Fetch repo info (searching for .git directory)
    # We traverse upwards from the file's location to find the root of the git repo
    git_root = None
    for parent in current_file.parents:
        if (parent / ".git").exists():
            git_root = parent
            break

    if not git_root:
        print("Error: File is not within a git repository.")
        sys.exit(1)

    # 3. Get owner of repo
    try:
        # Get the remote URL (origin) using git command line
        remote_url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], 
            cwd=str(git_root), 
            stderr=subprocess.STDOUT
        ).decode("utf-8").strip()

        # Parse owner from URL formats: 
        # https://github.com/owner/repo.git OR git@github.com:owner/repo.git
        if "github.com" in remote_url:
            if remote_url.startswith("http"):
                # URL: https://github.com/oktokat/repo
                owner = remote_url.split("github.com/")[1].split("/")[0]
            else:
                # URL: git@github.com:oktokat/repo.git
                owner = remote_url.split("github.com:")[1].split("/")[0]
        else:
            # Fallback for non-github repos or unexpected formats
            owner = None
            
    except subprocess.CalledProcessError:
        print("Error: Could not retrieve git remote information.")
        sys.exit(1)
    
    if owner is None:
        print("Error: Could not retrieve git user info.")
        sys.exit(1)

    # 4. Check if "SOLUTIONS" directory is present in same directory as file
    solutions_dir = current_dir / "SOLUTIONS"
    if not solutions_dir.is_dir():
        print(f"Error: 'SOLUTIONS' directory not found in {current_dir}")
        sys.exit(1)

    # 5. Check if <owner>_solutions exists
    target_folder_name = f"{owner}_solutions"
    target_path = solutions_dir / target_folder_name

    if target_path.exists():
        print(f"Directory '{target_folder_name}' already exists. Stopping.")
        return

    # 6. Create it and copy test_playground
    try:
        # Find test_playground in the same directory as the script
        playground_src = current_dir / "test_playground"
        
        if not playground_src.exists():
            print("Error: 'test_playground' directory not found to copy from.")
            sys.exit(1)

        # Create target and copy all components (shutil.copytree creates the destination)
        shutil.copytree(playground_src, target_path)
        print(f"Successfully created '{target_folder_name}' and copied 'test_playground' contents.")
        
    except Exception as e:
        print(f"An error occurred during directory creation/copying: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_solutions()