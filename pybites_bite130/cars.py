from collections import Counter

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    return Counter(
        entry["automaker"] for entry in data if entry["year"] == year
    ).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    return {
        entry["model"]
        for entry in data
        if entry["automaker"] == automaker and entry["year"] == year
    }
