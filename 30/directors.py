import csv
import operator
from collections import defaultdict, namedtuple
import os
from typing import MutableMapping, List, Tuple
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = "/tmp"

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director() -> MutableMapping:
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)

    with open(local) as f:
        for row in csv.DictReader(f):
            try:
                year = int(row["title_year"])
                if year < 1960:
                    continue
            except ValueError:
                # Skip records for which no year is provided
                continue

            movies_by_director[row["director_name"]].append(
                Movie(row["movie_title"].strip(), year, float(row["imdb_score"]))
            )

    return movies_by_director


def calc_mean_score(movies: Movie) -> float:
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    return round(sum(movie.score for movie in movies) / len(movies), 1)


def get_average_scores(directors: MutableMapping) -> List[Tuple[str, float]]:
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    scores = []
    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        scores.append((director, calc_mean_score(movies)))

    return sorted(scores, key=operator.itemgetter(1), reverse=True)
