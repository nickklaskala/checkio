#!/usr/bin/env checkio --domain=py run snake

# We all know the classic game"Snake".
# 
# You are given a 10x10 field of cells. You control a snake and your task is to eat 5 cherries which are randomly    placed on the field. The snake starts the game 5 units long and grows by one unit for each cherry it eats. In order    to survive long enough to eat the cherries, the snake must not hit a tree, the edge of the field, or its own body.    Doing so would trigger a game over. The snake does not sit still and is constantly moving. It can go in one of 3    directions: Forward “F”, Left “L” and Right “R”. Left and right are defined by the current position and trajectory    of the snakes head. The map of field is presented as list of strings, where:
# 
# 
#     "." - Empty cell
#     "T" - Tree
#     "C" - Cherry
#     "0" - Snake head
#     "1..9" -  Numbered Segments of the Snake Body
# 
# This is a multi-call task and your function will be called repeatedly until the game is complete. During each    function call, you can return a character or a string that contains a sequence of actions (example: “FRFLF.”) Once    the snake eats a cherry the remaining actions are dropped, a new cherry appears and the game continues. Once 5    cherries are eaten the game is over and you win. This version of snake has an interesting twist: you must eat the 5    cherries in 250 steps or less or face a game over.
# 
# 
# 
# At first the snake will move its tail then it will move its head. You can try to have your snake chase its tail this    way. Be careful if you use breadth first search -- it can take a long time if you select a bad state representation.
# 
# Input:The map of field as a list of strings.
# 
# Output:One or more actions as a string.
# 
# Precondition:|field| == 10 x 10
# New cherries can't appear in the outer cells (ex. [0,0], [9, 9]), but the start cherry can be in outer cells.
# 
# 
# 
# END_DESC

ACTION = ("L", "R", "F")
CHERRY = 'C'
TREE = 'T'
SNAKE_HEAD = '0'
SNAKE = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
EMPTY = "."


def snake(field_map):
    return "F" or "R" or "L" or "FRL"


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import randint

    def find_snake(field_map):
        snake = {}
        for i, row in enumerate(field_map):
            for j, ch in enumerate(row):
                if ch in SNAKE:
                    snake[ch] = (i, j)
        return snake

    def find_new_head(snake, action):
        head = snake[SNAKE_HEAD]
        snake_dir = (head[0] - snake["1"][0], head[1] - snake["1"][1])
        if action == 'F':
            return head[0] + snake_dir[0], head[1] + snake_dir[1]
        elif action == 'L':
            return head[0] - snake_dir[1], head[1] + snake_dir[0]
        elif action == 'R':
            return head[0] + snake_dir[1], head[1] - snake_dir[0]
        else:
            raise ValueError("The action must be only L,R or F")

    def pack_map(list_map):
        return [''.join(row) for row in list_map]

    def check_solution(func, field_map):
        temp_map = [list(row) for row in field_map]
        step_count = 250
        while True:
            route = func(field_map[:])
            res_route = ""
            for ch in route:
                if step_count < 0:
                    print("Too many steps (no more than 250)."),
                    return False
                if ch not in ACTION:
                    print("The route must contain only F,L,R symbols")
                    return False
                res_route += ch
                snake = find_snake(temp_map)
                tail = snake[max(snake.keys())]
                temp_map[tail[0]][tail[1]] = EMPTY
                new_head = find_new_head(snake, ch)
                for s_key in sorted(snake.keys())[:-1]:
                    s = snake[s_key]
                    temp_map[s[0]][s[1]] = str(int(temp_map[s[0]][s[1]]) + 1)
                if (new_head[0] < 0 or new_head[0] >= len(temp_map) or
                        new_head[1] < 0 or new_head[1] >= len(temp_map[0])):
                    print("The snake crawl outside")
                    return False
                elif temp_map[new_head[0]][new_head[1]] == 'T':
                    print("The snake struck at the tree")
                    return False
                elif temp_map[new_head[0]][new_head[1]] in SNAKE:
                    print("The snake bit itself")
                    return False

                if temp_map[new_head[0]][new_head[1]] == 'C':
                    temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
                    if max(snake.keys()) == '9':
                        return True
                    else:
                        temp_map[tail[0]][tail[1]] = str(int(max(snake.keys())) + 1)
                        cherry = (randint(1, len(temp_map) - 2),
                                  randint(1, len(temp_map[0]) - 2))
                        while temp_map[cherry[0]][cherry[1]] != EMPTY:
                            cherry = (randint(1, len(temp_map) - 2),
                                      randint(1, len(temp_map[0]) - 2))
                        temp_map[cherry[0]][cherry[1]] = CHERRY
                        step_count -= 1
                else:
                    temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
                step_count -= 1
                field_map = pack_map(temp_map)

    assert check_solution(checkio, [
        ".T.....T..",
        ".C........",
        ".....T....",
        "..T....T..",
        "..........",
        ".0...T....",
        ".1........",
        ".2.T...T..",
        ".3...T....",
        ".4........"]), "Basic map"
    assert check_solution(checkio, [
        "..T....T.C",
        ".......T..",
        "...TTT....",
        "..T....T..",
        "..T...T...",
        ".0T..T....",
        ".1........",
        ".2.T..TT..",
        ".3..TT....",
        ".4........"]), "Extra map"