#!/usr/bin/env checkio --domain=py run painting-wall

# Nicola has built a simple robot for painting of the wall.    The wall is marked at each meter and the robot has a list of painting operations.    Each operation describes which part of wall it needs to paint as a range from place to place, inclusively.    For example: the operation [1, 5] means to paint the sections from 1 to 5 meters including sections 1 and 5.    Operations are executed in the order they are placed in the list of operations.    If the range of various operations are overlapped, thenthey must be counted once.
# 
# Stephan has prepared a list of operations, but we need to check it before the robot executes its painting plan.    You are given the number of meters on the walls which need painting,    (the painted zones can be separated by non painted parts) and the list of operations prepared by Stephan,    you should determine the number of operations from this list required to paint the designated length of the wall.    If it's impossible to paint that length with the given operations, then return -1.
# 
# 
# 
# Input:Two arguments.The required length of the wall that should be painted, as integer.A list of the operations that contains the range (inclusive) as a list of two integers.
# 
# Output:The minimum number of operations. If you cannot paint enough of the length with the given operations, return -1.
# 
# Hint:To handle the beginning-end of the list, you could try running a binary search.
# 
# Precondition:
# 0 < len(operations) ≤ 30
# all(0 < x < 2 * 10 ** 18 and 0 < y < 2 * 10 ** 18 for x, y inoperations)
# 0 < required < 2 * 10 ** 18
# 
# 
# END_DESC

def checkio(required, operations):
    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"