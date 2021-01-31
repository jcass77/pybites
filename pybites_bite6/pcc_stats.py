import bisect
from collections import Counter, namedtuple
import os
import urllib.request

# prep
from distutils.util import strtobool

tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "dirnames")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt", tempfile
)

IGNORE = sorted("static templates data pybites bbelderbos hobojoe1848".split())

Stats = namedtuple("Stats", "user challenge")


def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile) as f:
        for line in f:
            name, is_dir = line.rstrip().rsplit(",", maxsplit=1)
            if strtobool(is_dir):
                yield name.lower()


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    pybites_bite1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    for dir_ in files:
        challenge, user = dir_.split("/")

        if ignore_user(user):
            continue

        users[user] += 1
        popular_challenges[challenge] += 1

    top_user = users.most_common(1)[0][0]
    top_challenge = popular_challenges.most_common(1)[0]

    return Stats(top_user, top_challenge)


def ignore_user(user):
    i = bisect.bisect_left(IGNORE, user)
    if i != len(IGNORE) and IGNORE[i] == user:
        return True
    return False
