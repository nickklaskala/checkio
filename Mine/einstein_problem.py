#!/usr/bin/env checkio --domain=py run einstein-problem

# The Einstein's Puzzleis a well-known logic puzzle.    It is often called Einstein's Puzzle because it is said to have been invented by Albert Einstein as a boy.    However, there is no known evidence for Einstein's or Carroll's authorship.    This puzzle can be modified with various conditions to produce a variety of similar puzzles. For starters, we will    solve a simplified version of the puzzle.
# 
# There are 5 houses on street which are painted 5 different colors:blue,green,red,whiteandyellow.
# In each house lives a person of a different nationality:Brit,Dane,German,NorwegianandSwede.
# These people drink a certain beverage:beer,coffee,milk,teaandwater.
# Smoke a certain brand of cigarettes:Rothmans,Dunhill,PallMall,WinfieldandMarlboro.
# They keep a certain pet:cat,bird,dog,fishandhorse.
# 
# None of the owners have the same pet, smoke the same brand of cigarette, or drink the same beverage.
# 
# You are given a set of "relations". Each relation connects two identifiers in the owner relationships. For example:    "Norwegian-Dunhill" indicates that the Norwegian smokes only Dunhill. "5-dog" indicates that the owner of the 5th    house also owns a dog. Similar to Einstein's version of the problem, we will use only these types of relations.
# 
# The second argument is a question which you need to answer. The question is represented as two words separated by    dash. The first word is a characteristic of the owner while the second is a characteristic (number,    color,nationality, beverage, cigarettes or pet) you need to determine based on the first characteristic. For    example: "horse-cigarettes" asks"What the cigarettes do the owner of the horse smoke?" or "green-number" asks "What    is the street number of the green house?".
# 
# Input:Two arguments. Relations as a tuple of strings and a question as a string.
# 
# Output:The answer as a string.
# 
# How it is used:This mission teaches you something about constraint satisfaction problems within the classic context of an Einstein riddle.
# 
# Precondition:
# All questions have only one possible answer.
# 
# 
# END_DESC

COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = ["number", "color", "nationality", "beverage", "cigarettes", "pet"]


def answer(relations, question):
    return "Answer"


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?