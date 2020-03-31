#!/usr/bin/env checkio --domain=py run sudokusolver

# Sudoku is a logic-based number-placement puzzle.    The objective is to fill a 9×9 grid with digits so that each column,    each row and each 3×3 sub-grid contains all of the digits from 1 to 9.    The puzzle creator provides a partially completed grid, which typically has a unique solution.
# 
# For more information about this game, you should report tothis site.
# 
# For example, the following grid
# 
# 
# gives the result:
# 
# 
# A puzzle is represented as a list of lists with digits.    A zero value means that the value hasn't been set.
# 
# Input:The initial 9x9 grid composed by integers as a list of lists.
# 
# Output:The result of the sudoku as a list of lists.
# 
# How it is used:This is a classic constraint satisfaction problem.    CSPs are mathematical problems defined as a set of objects whose state must satisfy a number of constraints or limitations.    CSPs are the subject of intense research in both artificial intelligence and operations research, since the regularity in their formulation provides a common basis to analyze and solve problems of many unrelated families.
# And of course now you can use this code to help your gramma solve all of the puzzles.
# 
# Precondition:Each test case has only one unique solution.
# ∀ x ∈ puzzle : 0 ≤ x<10
# 
# 
# 
# END_DESC

# Return the solution of the sudoku.
def checkio(grid):
    # Insert your code here.
    return [[0 for j in range(9)] for i in range(9)]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0],
                    [0, 4, 9, 7, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 5, 0, 4],
                    [0, 0, 0, 3, 0, 7, 0, 0, 0],
                    [2, 0, 3, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 0, 3, 7, 2, 0],
                    [0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
                                                      [8, 4, 9, 7, 2, 5, 3, 6, 1],
                                                      [5, 6, 2, 9, 3, 1, 4, 7, 8],
                                                      [6, 8, 7, 2, 1, 9, 5, 3, 4],
                                                      [9, 1, 4, 3, 5, 7, 2, 8, 6],
                                                      [2, 5, 3, 8, 4, 6, 1, 9, 7],
                                                      [1, 3, 6, 5, 7, 2, 8, 4, 9],
                                                      [4, 9, 8, 1, 6, 3, 7, 2, 5],
                                                      [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
    assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
                    [0, 0, 1, 0, 3, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 5, 9, 7, 2, 6, 4, 0],
                    [0, 0, 0, 6, 0, 1, 0, 0, 0],
                    [0, 2, 6, 3, 8, 5, 9, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 5, 0, 2, 0, 0],
                    [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
                                                      [9, 7, 1, 2, 3, 4, 5, 6, 8],
                                                      [2, 3, 4, 5, 6, 8, 7, 9, 1],
                                                      [1, 8, 5, 9, 7, 2, 6, 4, 3],
                                                      [3, 9, 7, 6, 4, 1, 8, 5, 2],
                                                      [4, 2, 6, 3, 8, 5, 9, 1, 7],
                                                      [6, 1, 9, 8, 2, 3, 4, 7, 5],
                                                      [7, 4, 3, 1, 5, 6, 2, 8, 9],
                                                      [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    print('Local tests done')