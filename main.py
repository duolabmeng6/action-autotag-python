import os
from pathlib import Path
from github import Github

def main():
    my_input = os.environ["INPUT_MYINPUT"]
    my_output = f"Hello {my_input}"
    variable = "1.0.0"

    print(f"::set-output name=myOutput::{my_output}")
    print(f"::set-output name=version::{variable}")

    g = Github(os.environ["INPUT_TOKEN"])
    repo = g.get_repo(os.environ["github"]["repository"])
    for tag in repo.get_tags():
        if tag.name == variable:
            return
    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{variable}", sha)



if __name__ == "__main__":
    main()