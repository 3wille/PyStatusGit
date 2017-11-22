from i3pystatus import IntervalModule
from git import Repo


class GitStatus(IntervalModule):
    """
    class fetches number of changed files from a specified local git
    repository
    Requires the PyPI package `GitPython`

    ..rubric:: Available formatters

    * `{path}` - path to git repository
    """
    format = ".dotfiles: {ch_files}"
    settings = (
        "path"
    )

    path = "~/.dotfiles"

    def run(self):
        repo = Repo(self.path)
        index = repo.index.diff(None)
        ch_files = len(index)
        self.output = {
            "full_text": self.format.format(ch_files=ch_files)
        }


def main():
    gs = GitStatus()
    gs.run()


if __name__ == "__main__":
    # execute only if run as a script
    main()
