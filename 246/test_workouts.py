import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "workout, days",
    [
        ("cardio", "Wed"),  # Single word
        ("CARdio", "Wed"),  # Case insensitive
        ("upper body", "Mon, Thu"),  # Multiple words
        ("body", "Mon, Tue, Thu, Fri"),  # Multiple matches
        ("march", "No matching workout"),  # No match
    ],
)
def test_print_workout_days(capsys, workout, days):
    print_workout_days(workout)
    captured = capsys.readouterr()
    assert captured.out.strip() == days
