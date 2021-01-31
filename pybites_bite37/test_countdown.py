import inspect

from countdown import countdown_for, countdown_recursive

expected = """10
9
pybites_bite8
7
pybites_bite6
pybites_bite5
pybites_bite4
3
2
pybites_bite1
time is up
"""
expected_other_start_arg = """pybites_bite13
12
11
"""
expected_other_start_arg += expected


def test_countdown_for(capfd):
    countdown_for()
    out, _ = capfd.readouterr()
    assert out == expected


def test_countdown_recursive(capfd):
    countdown_recursive()
    out, _ = capfd.readouterr()
    assert out == expected


def test_test_countdown_recursive_different_start(capfd):
    countdown_recursive(13)
    out, _ = capfd.readouterr()
    assert out == expected_other_start_arg


def test_recursion_used():
    func = countdown_recursive
    err = f"expecting {func.__name__} twice in your answer"
    assert inspect.getsource(func).count(func.__name__) == 2, err
