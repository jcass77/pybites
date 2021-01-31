from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple("State", "color command timeout")


def traffic_light():
    states = (
        State("red", "Stop", 2),
        State("green", "Go", 2),
        State("amber", "Caution", 0.5),
    )

    return cycle(states)


if __name__ == "__main__":
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f"{state.command}! The light is {state.color}")
        sleep(state.timeout)
