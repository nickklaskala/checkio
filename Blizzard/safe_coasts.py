#!/usr/bin/env checkio --domain=py run safe-coasts

# "I had often heard of the superstition of sailors respecting        apparitions, but had never given much credit to the        report; it seems that some years since a Dutch man-of-war was lost off        the Cape of Good Hope, and every soul on        board perished; her consort weathered the gale, and arrived soon after        at the Cape. Having refitted, and returning        to Europe, they were assailed by a violent tempest nearly in the same        latitude. In the night watch some of the        people saw, or imagined they saw, a vessel standing for them under a        press of sail, as though she would run them        down: one in particular affirmed it was the ship that had foundered in        the former gale, and that it must certainly        be her, or the apparition of her; but on its clearing up, the object, a        dark thick cloud, disappeared. Nothing could        do away the idea of this phenomenon on the minds of the sailors; and, on        their relating the circumstances when they        arrived in port, the story spread like wild-fire, and the supposed        phantom was called the Flying Dutchman. From the        Dutch the English seamen got the infatuation, and there are very few        Indiamen, but what has some one on board, who        pretends to have seen the apparition."
# -- George Barrington, "Voyage to Botany Bay"
# 
# After we have learnedhow    to recognize the Ghost shipwe identified it as the legendary"Flying Dutchman".    This knowledge gives us advantage, because we know that the ship can never    enter port or approach the coast. So, if    we have a regional map and the locations where Flying Dutchman typically    appears, then we can make a detailed map    with defined safe zones.
# 
# You are given a regional map as an array with strings, which is represented    as 2D array. Water cells are marked as"."and land cells as"X". Cells where the    Ghost Ship can appear are marked with a""D". You should finish the map    and mark (replace the relevant water cells) all of the safe cells with an"S"and the dangerous ones    as"D"(cells    the Ghost Ship can reach).
# 
# The Ghost Ship can move to neighbour cells at in the cardinal directions -    up, down, left, and right. It cannot move    to cells which are placed next to land including cells at the diagonals. So,    the safe cells are cells where Flying    Dutchman cannot approach from all possible directions.
# 
# 
# 
# 
# ("D..XX.....",        ("DDSXXSDDDD",
#  "...X......",         "DDSXSSSSSD",
#  ".......X..",         "DDSSSSSXSD",
#  ".......X..",         "DDSSSSSXSD",
#  "...X...X..",  ===\   "DDSXSSSXSD",
#  "...XXXXX..",  ===/   "SSSXXXXXSD",
#  "X.........",         "XSSSSSSSSD",
#  "..X.......",         "SSXSDDDDDD",
#  "..........",         "DSSSSSDDDD",
#  "D...X....D")         "DDDSXSDDDD")
# 
#     
# 
# Input:A regional map as a tuple of strings.
# 
# Output:The finished map as a list/tuple of strings.
# 
# Precondition:
# 3 ≤ len(regional_map) ≤ 10
# all(3 ≤ len(row) ≤ 10 and len(row) == len(regional_map[0]) for row in    regional_map)
# any("D" in row for row in regional_map)
# 
# 
# 
# END_DESC

def finish_map(regional_map):
    return regional_map


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"