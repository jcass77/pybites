import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "workouts",
    (
        ("upper body #1", ("mon",)),
        ("lower body #1", ("tue",)),
        ("30 min cardio", ("wed",)),
        ("upper body #2", ("thu",)),
        ("lower body #2", ("fri",)),
        ("upper body", ("mon", "thu")),
        ("lower body", ("tue", "fri")),
        ("upper", ("mon", "thu")),
        ("lower", ("tue", "fri")),
        ("body", ("mon", "tue", "thu", "fri")),
        ("#1", ("mon", "tue")),
        ("#2", ("thu", "fri")),
        ("30 min", ("wed",)),
        ("cardio", ("wed",)),
    ),
)
def test_print_workout_days_prints_correct_workouts(capsys, workouts):
    workout, workout_days = workouts
    print_workout_days(workout)
    days = [day.strip() for day in capsys.readouterr().out.lower().split(",")]
    assert set(days) == set(workout_days)


def test_workout_days_no_match_prints_no_matching_workout(capsys):
    print_workout_days("no such workout")
    assert capsys.readouterr().out.lower().strip() == "no matching workout"
