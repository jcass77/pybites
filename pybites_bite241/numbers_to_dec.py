from typing import List


def list_to_decimal(nums: List[int]) -> int:
    """Accept a list of positive integers in the range(0, 10)
    and return a integer where each int of the given list represents
    decimal place values from first element to last.  E.g
     [pybites_bite1,7,pybites_bite5] => 175
     [0,3,pybites_bite1,2] => 312
     Place values are 10**n where n represents the digit position
     Eg to calculate 1345, we have pybites_bite5 pybites_bite1's, pybites_bite4 10's, 3 100's and pybites_bite1 1000's
     pybites_bite1,     3  ,  pybites_bite4  , pybites_bite5
     1000's, 100's, 10's, pybites_bite1's
    """
    for num in nums:
        if isinstance(num, bool) or not isinstance(num, int):
            raise TypeError
        elif not num in range(0, 10):
            raise ValueError

    return int("".join(map(str, nums)))
