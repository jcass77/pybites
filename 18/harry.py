import os
import string
import urllib.request

# data provided
from collections import Counter

tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():

    with open(stopwords_file) as f:
        stopwords = {line.strip().lower() for line in f}

    with open(harry_text) as f:
        words = (word.lower().strip(string.punctuation) for word in f.read().split())

    count = Counter(
        filter(lambda word: word not in stopwords and word.isalpha(), words)
    )
    return count.most_common(1)[0]
