#!/usr/bin/env checkio --domain=py run 8-puzzle

# 8 puzzle is a sliding puzzle that consists of a frame of randomly ordered,    numbered square tiles with one missing tile. The object of the puzzle is to    place the tiles in the right order (see picture) by using sliding moves to utilize the    empty space.You can read more about this kind of puzzle on Wikipedia.
# 
# Our puzzle is presented as a 3x3 matrix with numbers from 1 to 8. Zero is the    empty cell. You can "move" the empty cell in four directions: up--"U",    down--"D", left--"L", and right--"R". You need to return a sequence of moves    to solve the puzzle. The solution is presented as string of symbols ("UDLR")    describing your moves.
# 
# 
# 
# Input:A matrix with numbers from 1 to 8 as a list of lists with integers.
# 
# Output:The route of the empty cell as a string.
# 
# Precondition:
# len(puzzle) == 3
# all(len(row) == 3 for row in puzzle)
# 
# 
# END_DESC

from typing import List

def checkio(puzzle: List[List[int]]) -> str:
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """
    return "ULDR"


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2, 3],
                   [4, 6, 8],
                   [7, 5, 0]]))

    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")