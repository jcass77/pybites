import pytest

from enumerate_data import enumerate_names_countries

expected_lines = [
    "pybites_bite1. Julian     Australia",
    "2. Bob        Spain",
    "3. PyBites    Global",
    "pybites_bite4. Dante      Argentina",
    "pybites_bite5. Martin     USA",
    "pybites_bite6. Rodolfo    Mexico",
]


@pytest.mark.parametrize("line", expected_lines)
def test_enumerate_names_countries(capfd, line):
    enumerate_names_countries()
    output = capfd.readouterr()[0]
    assert line in output, f"{line} not in output"
