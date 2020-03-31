#!/usr/bin/env checkio --domain=py run water-jars

# You stand by the edge of a lake with two empty jars. You notice that both of the jars have a volume.    You can fill each jar with water from the lake, pour water from one jar to the other or pour water back into lake.    You should measure the volume of water ineitherjar.    The required volume of water may be in either of the jars and it does not matter which.
# 
# Each action is described as a string of two symbols: from and to.    The jars are marked as1and2, the lake is marked0.    If you want to take water from the lake and fill first jar, then it's "01".     To pour water from second jar into the first would be "21".    Dump water out of the first jar and back into the lake would be "10".    When you fill a jar from the lake, that jars volume will be full.    When you pour water out a jar and into the lake, that jars volume will be empty.    If you pour water from one jar to another, you can only pour as much as will fill the full volume of the receiving jar.
# 
# 
# 
# The function has three arguments: The volume of first jar, the volume of second jar and the goal.    All arguments are positive integers (number > 0).    You should return a list with action's sequence.
# The solution must contain the minimum possible number of steps
# 
# Input:The volume of first jar, the volume of second jar and the goal as integers.
# 
# Output:The sequence of steps as a list/tuple with strings.
# 
# Precondition:
# 0 < first, second, goal < 10
# goal ≤ first or goal ≤ second
# All test cases have solution.
# 
# 
# END_DESC

def checkio(first, second, goal):
    #replace this for solution
    return []

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, initial_data, max_steps):
        first_volume, second_volume, goal = initial_data
        actions = {
            "01": lambda f, s: (first_volume, s),
            "02": lambda f, s: (f, second_volume),
            "12": lambda f, s: (
                f - (second_volume - s if f > second_volume - s else f),
                second_volume if f > second_volume - s else s + f),
            "21": lambda f, s: (
                first_volume if s > first_volume - f else s + f,
                s - (first_volume - f if s > first_volume - f else s),
            ),
            "10": lambda f, s: (0, s),
            "20": lambda f, s: (f, 0)
        }
        first, second = 0, 0
        result = func(*initial_data)
        if len(result) > max_steps:
            print("You answer contains too many steps. It can be shorter.")
            return False
        for act in result:
            if act not in actions.keys():
                print("I don't know this action {0}".format(act))
                return False
            first, second = actions[act](first, second)
        if goal == first or goal == second:
            return True
        print("You did not reach the goal.")
        return False

    assert check_solution(checkio, (5, 7, 6), 10), "Example"
    assert check_solution(checkio, (3, 4, 1), 2), "One and two"