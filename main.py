import os
from pathlib import Path
from github import Github


def main():
    with Path(os.environ["INPUT_PATH"]).open() as f:
        v = f.read()
    version_tag = f"{v}"
    os.environ['version'] = version_tag
    g = Github(os.environ["INPUT_TOKEN"])
    repo = g.get_repo(os.environ["github"]["repository"])
    for tag in repo.get_tags():
        if tag.name == version_tag:
            return
    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)

if __name__ == "__main__":
    main()
