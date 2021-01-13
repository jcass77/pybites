import itertools


def find_number_pairs(numbers, N=10):
    combinations = itertools.combinations(numbers, r=2)
    return [nums for nums in combinations if sum(nums) == N]
