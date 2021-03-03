from contextlib import nullcontext
from unittest.mock import patch

import pytest

from guess import GuessGame, InvalidNumber, MAX_NUMBER

SECRET_NUMBER = 5


@pytest.fixture
def game():
    return GuessGame(SECRET_NUMBER)


class TestGuessGame:
    def test_init_sets_defaults(self, game):
        assert game.max_guesses == 5
        assert game.attempt == 0

    @pytest.mark.parametrize(
        "guess, context, exception_type, args",
        (
            ("abc", pytest.raises, InvalidNumber, {"match": "Not a number"}),
            (-1, pytest.raises, InvalidNumber, {"match": "Negative number"}),
            (
                MAX_NUMBER + 1,
                pytest.raises,
                InvalidNumber,
                {"match": "Number too high"},
            ),
            (0, nullcontext, None, {}),
            (1, nullcontext, None, {}),
            (MAX_NUMBER - 1, nullcontext, None, {}),
            (MAX_NUMBER, nullcontext, None, {}),
        ),
    )
    def test_validate_all_permutations(
        self, guess, context, exception_type, args, game
    ):
        with context(exception_type, **args):
            game._validate(guess)

    @pytest.mark.parametrize(
        "user_input, expected",
        (
            (SECRET_NUMBER - 1, "Too low"),
            (SECRET_NUMBER + 1, "Too high"),
            (SECRET_NUMBER, "You guessed it!"),
        ),
    )
    def test_guess_all_permutations(
        self, capsys, game, user_input, expected, monkeypatch
    ):
        monkeypatch.setattr(game, "max_guesses", 1)
        with patch(
            "builtins.input",
            return_value=user_input,
        ):
            game()

        out, err = capsys.readouterr()

        assert out.splitlines()[1] == expected

    def test_guess_not_a_number_repeats_attempt(self, capsys, game):
        with patch("builtins.input", side_effect=["abc", game.secret_number]):
            game()

        out, err = capsys.readouterr()

        assert out.splitlines() == [
            "Guess a number: ",
            "Enter a number, try again",
            "Guess a number: ",
            "You guessed it!",
        ]

    def test_invalid_attempts_does_not_increment_number_of_attempts(self, capsys, game):
        with patch("builtins.input", side_effect=["abc", "xyz", game.secret_number]):
            game()

        assert game.attempt == 1

    def test_guess_max_guesses_exceeded_prints_sorry_message(
        self, capsys, game, monkeypatch
    ):
        monkeypatch.setattr(game, "max_guesses", 1)
        with patch("builtins.input", side_effect=[0]):
            game()

        out, err = capsys.readouterr()

        assert out.splitlines()[-1] == f"Sorry, the number was {SECRET_NUMBER}"
