from typing import List


def uncommon_cities(my_cities: List[str], other_cities: List[str]):
    """Compare my_cities and other_cities and return the number of different
    cities between the two"""
    return len(set(my_cities) ^ set(other_cities))
