import json
import re
from collections import Counter


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_data = []
    for file in files:
        with open(file) as f:
            movie_data.append(json.loads(f.read()))

    return movie_data


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "comedy" in movie["Genre"].lower():
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominated_for_pattern = r"(?:nominated for )(\d+)"
    nominations_pattern = r"(\d+)(?: nomination[s*])"
    num_nominations = Counter()

    for movie in movies:
        for pattern in (nominated_for_pattern, nominations_pattern):
            try:
                num_nominations[movie["Title"]] += sum(
                    int(num)
                    for num in re.findall(
                        pattern, movie["Awards"], re.MULTILINE | re.IGNORECASE
                    )
                )
            except AttributeError:
                # No match - skip
                pass

    return num_nominations.most_common(1)[0][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtimes = Counter(
        {movie["Title"]: int(movie["Runtime"].split()[0]) for movie in movies}
    )

    return runtimes.most_common(1)[0][0]
