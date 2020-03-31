#!/usr/bin/env checkio --domain=py run minesweeper

# "Nikola, what’s wrong with Stephen?" Sofia shouted in fear when she saw Nikola poking his tools inside        Stephen’s leg.
# 
# "He stepped on a landmine."
# 
# "What!?"
# 
# "Don't worry. The robots in his class have an extremely strong frame unlike us; he was mostly unscathed by the        explosion. Once I double check everything, I’ll send him in for cleaning."
# 
# "But where did he even find the landmine?"
# 
# "Yes, that's the question we should be worrying about. There's a landmine field about a 2 hour walk away from        here. It looks like somebody is protecting something, or maybe protecting themselves from something. However,        there is no easy way to cross that field.
# 
# "Is Stephen conscious now? Can he hear us?"
# 
# "No, but I know what you want to ask and my answer is no! We are not going to let Stephen clear a path through        the field for us. Even his fireproof frame will not be able to endure the blasts for that long. Plus it’s an        extremely unpleasant activity."
# 
# "How could you think that I would even ask something like that?" Sofia said angrily.
# 
# "So what was your question about then?"
# 
# "It doesn’t matter…so what do you propose? What are our options?"
# 
# "We will let you go there," said Nikola.
# 
# "What?! My frame isn't as strong as Stephen’s! No. No. No. I may be beautiful and expensive, but that doesn't        mean I am durable and reliable."
# 
# "There is a magnetic field there so every landmine is drawn to a metallic frame."
# 
# "Oh, so it won't be as bad if I go there?"
# 
# "Exactly. You have almost no metallic details --you can easily move around there."
# 
# "Even though your knowledge has never failed me, I would still love to put it to the test," said Sofia while        looking for something in the ship database. But, wait! I can't go there without you and, at the same time, I        can't leave you alone here."
# 
# "You're right--I don’t want you to go there alone. That's why I will give you a device that will not only show        you where the mines are, but it will also indicate the strength of the magnetic field around them. This will        help us know how many landmines there are around a particular cell and, based on that data, determine where the        landmines are."
# 
# "Okay, give me that device so that I can go around the field and make a map."
# 
# "Don’t rush--it’s not that easy. If you step on a landmine we will need many expensive, and pretty, details.        We'll need to write a module that will calculate the landmines' locations while you're moving along the route so        that you don't accidentally step on them."
# 
# "We'll have to write this module very carefully, correct? I want to be able to look you in the eyes, Mr. Smarty        Pants, from the safety of the other side of the field."
# 
# Minesweeper is a popular classic computer game.     The object of the game is to clear an abstract minefield without detonating a mine.    The player is initially presented with a grid of undifferentiated squares.     Some randomly selected squares, unknown to the player, contain mines.     The size of the grid is typically 10x10.    The game is played by revealing various squares of the grid.     If a square containing a mine is revealed, it detonates and the player loses the game.    When a non-mined square is clicked, a digit is revealed in the square.    This indicates the number of adjacent squares (typically, out of the possible eight) that contain mines.     In typical implementations, if this number is zero then the square appears blank, and the surrounding squares are automatically revealed.    You should open all cells without mine or mark all mines.
# 
# Let's learn the rules:- If you uncover a mine, the game ends.- If you uncover an empty square, you can keep playing.- If you mark as mine a mined cell, you can keep playing.- If you uncover a number, it will tell you how many mines lay hidden beneath the eight surrounding            squares—use this information to deduce which nearby squares are safe to click on.- If you mark as mine a cell without mine, the game ends.- If you uncover already opened cell, the game ends (we don't like perpetual game.).On each iteration, the checkio function got a field's map as argument. The map is presented as a list of list.    Each cell on the map can be marked as:-1-- not opened cells,9-- a mine,a number from 0 to 8-- a count of the    number of mines surrounding the cell.    Your checkio function must return a tuple or a list of three values. The first value reflects whether there is a    landmine on the following coordinates (true or false). The second and third values are the coordinates in the    passed field map (field[i][j]). For starting the game you can use [0, 0] cell -- it is empty always.
# 
# 
# 
# Input:A field map as a list of lists with integeres.
# 
# Output:A tuple or a list with next values: is it a mine as boolean, row and column as integers.
# 
# Precondition:
# len(field) == 10
# all(len(row) == 10 for rown in field)
# field[0][0] == 0
# The puzzle is solvable without random guessing.
# 
# 
# END_DESC

def checkio(field):
    return [False, 0, 0]

#This part is using only for self-testing
if __name__ == '__main__':

    def check_is_win_referee(input_map):
        unopened = [1 for x in range(10) for y in range(10) if input_map[x][y] == -1]
        return not unopened

    def build_map(input_map, mine_map, row, col):
        opened = [(row, col)]
        while opened:
            i, j = opened.pop(0)
            neighs = [(i + x, j + y) for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                      if 0 <= i + x < 10 and 0 <= j + y < 10]
            value = sum([mine_map[k][l] for k, l in neighs])
            input_map[i][j] = value
            if not value:
                for k, l in neighs:
                    if input_map[k][l] == -1 and (k, l) not in opened:
                        opened.append((k, l))
        return input_map

    def check_solution(func, mine_map):
        input_map = [[-1] * 10 for _ in range(10)]
        while True:

            is_mine, row, col = func([row[:] for row in input_map])  # using copy
            if input_map[row][col] != -1:
                print("You tried to uncover or mark already opened cell.")
                return False
            if is_mine and not mine_map[row][col]:
                print("You marked the wrong cell.")
                return False
            if not is_mine and mine_map[row][col]:
                print("You uncovered a mine. BANG!")
                return False
            if is_mine:
                input_map[row][col] = 9
            else:
                build_map(input_map, mine_map, row, col)
            if check_is_win_referee(input_map):
                return True
        return False

    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Simple"

    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), "Gate"

    assert check_solution(checkio, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]), "Various"