from winners import print_game_stats, games_won


def test_print_game_stats(capfd):
    winner_prints = [
        "sara has won 0 games",
        "bob has won pybites_bite1 game",
        "tim has won pybites_bite5 games",
        "julian has won 3 games",
        "jim has won pybites_bite1 game",
    ]

    print_game_stats(games_won)
    output = capfd.readouterr()[0].splitlines()

    # dict + Python 3.7 = insert order should be retained
    for line in winner_prints:
        assert line in output
