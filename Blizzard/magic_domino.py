#!/usr/bin/env checkio --domain=py run magic-domino

# When Nikola can not find opponent for a game ofDominoes,    he spreads them out for a game of Magic Domino Solitaire.    The goal of solitaire is to build aMagic squarewithDouble Sixdomino tiles.
# 
# A magic square is an arrangement of distinct integers, in a square grid,    where the numbers in each row, and in each column, and the numbers in the forward and backward main diagonals,    all add up to the same number.
# Domino tiles contain two numbers from 0 (empty) to 6. Tiles are unordered and 1-6 is the same as 6-1.    The double-six set contains 28 unique tiles - all combinations of number pairs.
# 
# 
# 
# You are given asizefor the magic square and anumber.    You should build a magic square to the givensizeso that the sum of the horizontal and vertical diagonals equal the givennumber.    You can place domino tiles from double-six set onlyverticallyand they should beunique.
# 
# Here is example forsize= 4 andnumber= 5:
# 
# 
# 
# The result magic square should be represented as a list/tuple of lists/tuples with integers.
# 
# Input:Two arguments. A magic square size and a number as integers
# 
# Output:The magic square as a list/tuple of lists/tuples with integers.
# 
# How it is used:This is a constraint satisfaction problem.    It's used not only for solving games of solitaire, but also for planning and resource allocation in city planning,    construction and just about anything else.
# 
# Precondition:
# size in (4, 6)
# All input test cases are solvable.
# 
# 
# END_DESC

def magic_domino(size, number):
    return ((1,) * size,) * size


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    import itertools

    def check_data(size, number, user_result):

        # check types
        check_container_type = lambda o: any(map(lambda t: isinstance(o, t), (list, tuple)))
        check_cell_type = lambda i: isinstance(i, int)
        if not (check_container_type(user_result) and
                all(map(check_container_type, user_result)) and
                all(map(lambda row: all(map(check_cell_type, row)), user_result))):
            raise Exception("You should return a list/tuple of lists/tuples with integers.")

        # check sizes
        check_size = lambda o: len(o) == size
        if not (check_size(user_result) and all(map(check_size, user_result))):
            raise Exception("Wrong size of answer.")

        # check is it a possible numbers (from 0 to 6 inclusive)
        if not all(map(lambda x: 0 <= x <= 6, itertools.chain.from_iterable(user_result))):
            raise Exception("Wrong matrix integers (can't be domino tiles)")

        # check is it a magic square
        seq_sum_check = lambda seq: sum(seq) == number
        diagonals_indexes = zip(*map(lambda i: ((i, i), (i, size - i - 1)), range(size)))
        values_from_indexes = lambda inds: itertools.starmap(lambda x, y: user_result[y][x], inds)
        if not (all(map(seq_sum_check, user_result)) and  # rows
                all(map(seq_sum_check, zip(*user_result))) and  # columns
                all(map(seq_sum_check, map(values_from_indexes, diagonals_indexes)))):  # diagonals
            raise Exception("It's not a magic square.")

        # check is it domino square
        tiles = set()
        for x, y in itertools.product(range(size), range(0, size, 2)):
            tile = tuple(sorted((user_result[y][x], user_result[y + 1][x])))
            if tile in tiles:
                raise Exception("It's not a domino magic square.")
            tiles.add(tile)

    check_data(4, 5, magic_domino(4, 5))