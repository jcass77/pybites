import os
import string
import urllib.request

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
        words = (word.strip(string.punctuation) for word in f.read().lower().split())
        words = (word for word in words if word and word not in stopwords)

    count = Counter(words)
    return count.most_common(1)[0]
