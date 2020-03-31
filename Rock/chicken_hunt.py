#!/usr/bin/env checkio --domain=py run chicken-hunt

# "It is plain indeed that in spite of later estrangement Hobbits are relatives of ours: far        nearer to us than        Elves, or even than Dwarves. Of old they spoke the languages of Men, after their own        fashion, and liked and        disliked much the same things as Men did. But what exactly our relationship is can no longer        be discovered."
# 
# "Hobbits are an unobtrusive but very ancient people, more numerous formerly than they are        today; for they love        peace and quiet and good tilled earth: a well-ordered and well-farmed countryside was their        favourite haunt."
# 
# -- "The Lord of the Rings" J.R.R.TolkienTwo Hobbits are trying to catch a chicken in the yard. It should be an easy task, but these two    neighbours never seem to get along. Now a chicken got loose and they need to catch it, but they    refuse to talk to each other. So, we need to find an algorithm which will work for the both of    the Hobbits independently, allowing either of them to catch a chicken without walking into a    fence, tree or each other. One last thing, Hobbits cannot run or wait forever. After all.    catching the chicken is important, but Hobbits must adhere to their strict dinner schedule.
# 
# You are given a yard map as a sequence of strings where:
# - "." is an empty cell;
# - "I" is managed Hobbit;
# - "S" is companion;
# - "C" is chicken (our target);
# - "X" is obstacle (a tree, a rock etc)
# 
# The yard is surrounded by a fence.
# 
# The chicken and Hobbits can move in 8 direction into neighbouring cells (including diagonals).    And they can wait and stay in one place for a while.    Actions are described with the following strings:
# - "N" north, "S" south, "W" west, "E" east;
# - "NW" north-west, "NE" north-east, "SW" south-west, "SE" south-east;
# - "" (empty string) is to wait.
# 
# The Chicken is unpredictable and can use various tactics (including random movement), but he can    not go out of the yard. Hobbits can not run in obstacles or in fences. And they should not    struck each other, even for the final jump by the chicken.
# 
# Now for the tricky part. Your function will be called twice in each step - once for the first    Hobbit and once for the second Hobbit. The Hobbits cannot communicate with each other and make    their moves simultaneously. So be careful with moving both Hobbits into one square. You should    move a Hobbit into the chickens square to win, but only one should make the move as two hobbits    entering the same cell would count as them colliding. The Hobbits and the chicken move    simultaneously, so if you just jump to a cell where is chicken, then is not guaranteed that you    will catch it. Since dinner time is coming soon for the Hobbits, you have no more 100 moves to    catch the chicken.
# 
# This is a "multicall" mission and your function will be called until you win or lose. Each cycle    of steps is running in a new environment, so you can use global variables between steps, but for    the new "hunt" they will be reseted..
# 
# This map will be looked little different for each function call:
# 
# 
#  First       Second
# "......",   "......",
# ".I.XX.",   ".S.XX.",
# "...CX.",   "...CX.",
# ".XX.X.",   ".XX.X.",
# "...S..",   "...I..",
# "......",   "......",
# 
#     
# 
# Input:A yard map as a tuple of strings. Your function is called twice for    each step.
# 
# Output:The action as a string. One of ("N", "S", "W", "E", "NW", "NE", "SW",    "SE", "S").
# 
# Precondition:
# 3 < len(yard) ≤ 10
# all(3 < len(row) ≤ 10 and len(row) == len(yard[0]) for row in yard)
# 
# 
# END_DESC

DIRS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NW": (-1, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "": (0, 0),
}


def hunt(yard):
    return "N"


if __name__ == "__main__":
    # These checker is using only for your local testing
    # It's run function in the same environment, but in the grading it will be in various
    from random import choice
    from re import sub
    from math import hypot

    def random_chicken(_, possible):
        return choice(possible)


    def distance_chicken(func):
        def run_chicken(yard, possible):
            enemies = [find_position(yard, str(i + 1)) for i in range(N)]
            best = "", find_position(yard, "C")
            best_dist = 0 if func == max else float("inf")
            for d, (x, y) in possible:
                min_dist = min(hypot(x - ex, y - ey) for ex, ey in enemies)
                if func(min_dist, best_dist) == min_dist:
                    best = d, (x, y)
                    best_dist = min_dist
                elif min_dist == best_dist:
                    best = choice([(d, (x, y)), best])
                print(best, best_dist)
            return best

        return run_chicken


    CHICKEN_ALGORITHM = {
        "random": random_chicken,
        "run_away": distance_chicken(max),
        "hunter": distance_chicken(min)
    }

    ERROR_TYPE = "Your function must return a direction as a string."
    ERROR_FENCE = "A hobbit struck in the fence."
    ERROR_TREE = "A hobbit struck in an obstacle."
    ERROR_HOBBITS = "The Hobbits struck each other."
    ERROR_TIRED = "The Hobbits are tired."

    N = 2

    MAX_STEP = 100

    def find_position(yard, symb):
        for i, row in enumerate(yard):
            for j, ch in enumerate(row):
                if ch == symb:
                    return i, j
        return None, None

    def find_free(yard, position):
        x, y = position
        result = [("", position)]
        for k, (dx, dy) in DIRS.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(yard) and 0 <= ny < len(yard[0]) and yard[nx][ny] == ".":
                result.append((k, (nx, ny)))
        return result

    def prepare_yard(yard, numb):
        return tuple(sub("\d", "S", row.replace(str(numb), "I")) for row in yard)

    def checker(func, yard, chicken_algorithm="random"):
        for _ in range(MAX_STEP):
            individual_yards = [prepare_yard(yard, i + 1) for i in range(N)]
            results = [func(y) for y in individual_yards]
            if any(not isinstance(r, str) or r not in DIRS.keys() for r in results):
                print(ERROR_TYPE)
                return False
            chicken = find_position(yard, "C")
            possibles = find_free(yard, chicken)
            chicken_action, new_chicken = CHICKEN_ALGORITHM[chicken_algorithm](yard, possibles)
            positions = [find_position(yard, str(i + 1)) for i in range(N)]
            new_positions = []
            for i, (x, y) in enumerate(positions):
                nx, ny = x + DIRS[results[i]][0], y + DIRS[results[i]][1]
                if not (0 <= nx < len(yard) and 0 <= ny < len(yard[0])):
                    print(ERROR_FENCE)
                    return False
                if yard[nx][ny] == "X":
                    print(ERROR_TREE)
                    return False
                new_positions.append((nx, ny))
            if len(set(new_positions)) != len(new_positions):
                print(ERROR_HOBBITS)
                return False

            if any(new_chicken == pos for pos in new_positions):
                print("Gratz!")
                return True

            # update yard
            temp_yard = [[ch if ch in ".X" else "." for ch in row] for row in yard]
            for i, (x, y) in enumerate(new_positions):
                temp_yard[x][y] = str(i + 1)
            temp_yard[new_chicken[0]][new_chicken[1]] = "C"
            yard = tuple("".join(row) for row in temp_yard)
        print(ERROR_TIRED)
        return False

    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "random"), "Example 1"
    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "run_away"), "Example 1"
    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "hunter"), "Example 1"

    assert checker(hunt, ("1.........",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.XCX.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".........2"), "run_away"), "Tunnels"
    assert checker(hunt, ("1X.X.X.X2",
                          "X.X.X.X.X",
                          ".X.X.X.X.",
                          "X.X.X.X.X",
                          ".X.X.X.X.",
                          "X.X.X.X.X",
                          ".X.XCX.X.",
                          "X.X.X.X.X")), "ChessBoard"
    assert checker(hunt, ("...2...",
                          ".......",
                          ".......",
                          "...C...",
                          ".......",
                          ".......",
                          "...1...")), "Clear Random"