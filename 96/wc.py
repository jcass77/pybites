import re
import string


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""
    num_words = num_chars = 0

    with open(file_) as f:
        lines = f.readlines()
        num_lines = len(lines)

        for line in lines:
            num_words += len(line.split())
            num_chars += len(line)

    return f"{num_lines} {num_words} {num_chars} {file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
