from collections import Counter
from pathlib import Path


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """
    if type(directory) is str:
        directory = Path(directory)

    count = Counter()
    for x in directory.iterdir():
        if x.is_dir():
            count["dir"] += 1
            count["file"] += count_dirs_and_files(x)[1]
        elif x.is_file():
            count["file"] += 1

    return count["dir"], count["file"]
