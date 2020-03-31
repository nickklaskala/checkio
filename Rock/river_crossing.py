#!/usr/bin/env checkio --domain=py run river-crossing

# 'River crossing puzzle' is the famous classic puzzle.    (also known asWolf, goat and cabbage problem)
# 
# summary:
# 
# The farmer needs to carry wolf, goat and cabbage by boat across the river.Only one can be loaded on the boat at a time.Don't leave wolf and goat on the bank (wolf eats goat).Don't leave goat and cabbage on the bank (goat eats cabbage).This time, I will extend this puzzle a little.    The number of wolves, goat, cabbages and payload is arbitrary.
# (see precondition)
# 
# You are given four integers as the number of wolves, goats, cabbages and payload of the boat.You have to return the minimum number of boat crossings required to carry all the loads.(If not possible, return None.)
# 
# NOTE:
# 
# All loads can live together on the boat.
# END_DESC

def river_crossing(wolves, goats, cabbages, payload):
    return None


if __name__ == '__main__':
    print("Example:")
    print (river_crossing(1, 1, 1, 1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert river_crossing(1, 1, 1, 1) == 7, 'original'
    assert river_crossing(1, 1, 1, 2) == 3, 'payload +1'
    assert river_crossing(2, 1, 1, 2) == 5, 'payload +1, wolf +1'
    assert river_crossing(1, 2, 1, 1) is None, 'impossible'
    print("Coding complete? Click 'Check' to earn cool rewards!")