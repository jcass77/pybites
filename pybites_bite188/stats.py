import os
import statistics
from typing import List
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DATA = "testfiles_number_loc.txt"
STATS = os.path.join(TMP, DATA)
if not os.path.isfile(STATS):
    urlretrieve(os.path.join(S3, DATA), STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def get_all_line_counts(data: str = STATS) -> List[int]:
    with open(data) as f:
        return [int(line.lstrip().split(" ", maxsplit=1)[0]) for line in f.readlines()]


def create_stats_report(data: List[int] = None) -> str:
    data = data or get_all_line_counts()

    sample = data[::2]

    stats = dict(
        count=len(data),
        min_=min(data),
        max_=max(data),
        mean=statistics.mean(data),
        pstdev=statistics.pstdev(data),
        pvariance=statistics.pvariance(data),
        sample_count=len(sample),
        sample_stdev=statistics.stdev(sample),
        sample_variance=statistics.variance(sample),
    )

    return STATS_OUTPUT.format(**stats)
