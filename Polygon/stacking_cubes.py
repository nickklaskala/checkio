#!/usr/bin/env checkio --domain=py run stacking-cubes

# This is a mission to stacking cubes.
# 
# You are given a list of cube details (tuple of 3 integers: X coordinate, Y coordinate, edge length).
# You have to return the largest in stacking height of the cubes.
# 
# Each coordinate is the minimum value.All edges parallel to the coordinate axes.The order of stacking the cubes is arbitrary, but the X and Y coordinates of the cubes can't be changed.if at least 1x1 faces touch, they will be stacked.Note :
# 
# You don't always need to use the all cubes.Input :A list of tuples of 3 integers.
# 
# Output :An integer.
# 
# Precondition :
# 
# 2 ≤ len(cubes) ≤ 50-100 ≤ X, Y coordinate ≤ 100
# END_DESC

from typing import List, Tuple


def stacking_cubes(cubes: List[Tuple[int, int, int]]) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    assert stacking_cubes([(0, 0, 2), (1, 1, 2), (3, 2, 2)]) == 4, 'basic'
    assert stacking_cubes([(0, 0, 2), (1, 1, 2), (1, 2, 1), (2, 2, 2)]) == 6, 'basic 2'
    assert stacking_cubes([(0, 0, 2), (2, 0, 2), (2, 0, 2), (0, 2, 2), (0, 2, 2), (0, 2, 2), (0, 2, 2)]) == 8, 'towers'
    assert stacking_cubes([(0, 0, 2), (0, 3, 2), (3, 0, 2)]) == 2, 'no stacking'
    assert stacking_cubes([(-1, -1, 2), (0, 0, 2), (-2, -2, 2)]) == 6, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")