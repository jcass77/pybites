import os
import random
import string

import pytest

from movies import MovieDb

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = os.path.join(os.getenv("TMP", "/tmp"), f"movies_{salt}.db")
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = "movies"


@pytest.fixture
def db():
    db_ = MovieDb(DB, DATA, TABLE)
    db_.init()
    yield db_
    db_.drop_table()


class TestMovieDb:
    @pytest.mark.parametrize(
        "query_params, expected",
        (
            ({"title": "Citizen Kane"}, [("Citizen Kane", 1941, 8.3)]),
            ({"year": 1941}, [("Citizen Kane", 1941, 8.3)]),
            (
                {"score_gt": 9},
                [("The Godfather", 1972, 9.2), ("The Shawshank Redemption", 1994, 9.3)],
            ),
            ({"title": "Wizard"}, [("The Wizard of Oz", 1939, 8)]),
            ({"title": "no_such_entry"}, []),
        ),
        ids=("by_tile", "by_year", "by_score", "partial_title", "does_not_exist"),
    )
    def test_query_returns_correct_results(self, db, query_params, expected):
        results = db.query(**query_params)
        result_num = None
        for result_num, entry in enumerate(results):
            assert entry[-3:] == expected[result_num]

        if result_num is None:
            assert results == expected

    def test_add_adds_entry(self, db):
        dummy_movie = ("Some movie", 2021, 4.3)
        idx = db.add(*dummy_movie)

        result = db.query("Some movie", 2021, 4.3)

        assert len(result) == 1
        assert result[0] == (idx, *dummy_movie)

    def test_delete_deletes_entry(self, db):
        idx = db.query("Lawrence of Arabia", 1962, 8.3)[0][0]
        db.delete(idx)
        assert not db.query("Lawrence of Arabia", 1962, 8.3)
