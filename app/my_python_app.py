"""
my Python app
"""
from git import Repo
import sys

def get_hash(repo_path):
    """
    returns the current commit hash
    """
    repo = Repo(repo_path)
    head_commit = repo.head.commit
    print(head_commit)
    print(head_commit.hexsha)


def main():
    """
    main function
    """
    repo_path = sys.argv[1]
    print("Hello, World")
    get_hash(repo_path)
    return 0

if __name__ == "__main__":
    main()
