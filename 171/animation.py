from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
    Takes seconds argument = time for the spinner to run.
    Does not return anything, only prints to stdout."""
    state = cycle(SPINNER_STATES)
    end_time = time() + seconds

    while time() < end_time:
        sys.stdout.write(f"{next(state)}\r")
        sleep(STATE_TRANSITION_TIME)


if __name__ == "__main__":
    spinner(2)
