import itertools
from collections import defaultdict
import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def _get_lines(log):
    with open(log) as f:
        yield from f.readlines()


def create_chart(log=None):
    line_gen1, line_gen2 = itertools.tee(_get_lines(log), 2)

    posts = defaultdict(list)

    for prev_line, line in zip(
        itertools.islice(line_gen1, 0, None, 1), itertools.islice(line_gen2, 1, None, 1)
    ):
        if "sending to" in line:
            date = prev_line.split()[0]
            book_icon = PY_BOOK if "python" in prev_line.lower() else OTHER_BOOK
            posts[date].append(book_icon)

    for date, books in posts.items():
        print(date, "".join(books))
