import datetime
import os
import urllib.request
from typing import List

SHUTDOWN_EVENT = "Shutdown initiated.\n"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line: str) -> datetime:
    ts = line.split(maxsplit=3)[1]
    return datetime.datetime.fromisoformat(ts)


def time_between_shutdowns(loglines: List[str]) -> datetime.timedelta:
    first_shutdown = None
    last_shutdown = None

    for line in loglines:
        if line.endswith(SHUTDOWN_EVENT):
            first_shutdown = convert_to_datetime(line)
            break

    for line in reversed(loglines):
        if line.endswith(SHUTDOWN_EVENT):
            last_shutdown = convert_to_datetime(line)
            break

    return last_shutdown - first_shutdown
