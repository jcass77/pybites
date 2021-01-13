from typing import List
from itertools import combinations, permutations


def friends_teams(
    friends: List[str], team_size: int = 2, order_does_matter: bool = False
):
    func = permutations if order_does_matter else combinations
    return func(friends, r=team_size)