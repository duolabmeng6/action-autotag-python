import os
from pathlib import Path
from github import Github

def main():
    Name = os.environ['GITHUB_ACTION_REPOSITORY']
    my_output = f"Hello {Name}"
    print("all environ")
    print(os.environ)

    variable = "1.0.0"
    print(f"::set-output name=myOutput::{my_output}")
    print(f"::set-output name=version::{variable}")

if __name__ == "__main__":
    main()