import git
import os

# Replace with your GitHub username and repository name
github_username = "cheryl-toh"
repo_name = "temp-repo"

# Path to the file you want to commit (replace with your actual file path)
file_name = "test.py"
file_path = f"/home/pi/Temp/temp-repo/{file_name}"  # Adjust the path as needed

# Function to commit changes to GitHub
def commit_to_github(file_path, commit_message="Update file"):
    try:
        # Change directory to repository directory
        os.chdir("/home/pi/Temp/temp-repo")

        # Initialize the repository object
        repo = git.Repo()

        # Configure user identity if not already configured
        if not repo.config_reader().has_option('user', 'email'):
            repo.git.config('user.email', 'cheryltqr@yahoo.com')
        if not repo.config_reader().has_option('user', 'name'):
            repo.git.config('user.name', 'cheryl-toh')

        # Stage the changes
        repo.git.add(file_path)

        # Commit the changes
        repo.index.commit(commit_message)

        # Push the changes to the remote repository (main branch)
        origin = repo.remote(name='origin')
        origin.push(refspec=f"HEAD:refs/heads/main")

        print("Changes committed and pushed to GitHub successfully.")
    except Exception as e:
        print(f"Error committing and pushing to GitHub: {e}")

if __name__ == "__main__":
    try:
        # Commit changes to GitHub
        commit_to_github(file_path, commit_message="Update test.py file")

    except Exception as e:
        print(f"Error: {e}")
