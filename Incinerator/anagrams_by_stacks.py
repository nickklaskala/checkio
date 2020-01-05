#!/usr/bin/env checkio --domain=py run anagrams-by-stacks

# You have been given two anagrams as a string, separated by dash.    You need to rearrange the letters to turn the first word into the second.    The tools you have for this mission are two stacks and a one-letter buffer.    The first stack is the beginning of a word; the second stack is where you will put the anagram.    The word is placed in the stack, letter by letter.    The first letter of the anagram is placed in the bottom stack and    the last letter in the middle stack, until it is needed as the end of the anagram.    You need to return the shortest sequence of actions to move and    turn the word in the first stack into the anagram in the second.    The first stack is labeled 1, the second is labeled 2, and    the buffer as 0. The action is written as a string of two numbers    which signify the original location of the letter and the new location.    For example: 12 means that from the first stack, we take the last letter and    place it at the end of the second stack. For the result,    you need to get a string that lists the steps, separated by commas.
# 
# 
# 
# Input:Two words separated by dash as a string.
# 
# Output:A sequence of actions as a string.
# 
# Precondition:1 ≤ |word|<10
# Words contains only ASCII letters in lowercase.
# 
# 
# END_DESC

def checkio(data):
    return ""


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOOD_ACTIONS = ("12", "10", "01", "02", "20", "21")

    def check_solution(func, anagrams, min_length):
        start, end = anagrams.split("-")
        stacks = [[], list(start), []]
        user_result = func(anagrams)
        actions = user_result.split(",")
        user_actions = []
        for act in actions:
            if act not in GOOD_ACTIONS:
                print("Wrong action")
                return False
            from_s = int(act[0])
            to_s = int(act[1])
            if not stacks[from_s]:
                print("You can not get from an empty stack")
                return False
            if to_s == 0 and stacks[to_s]:
                print("You can not push in the full buffer")
                return False
            stacks[to_s].append(stacks[from_s].pop())
            user_actions.append(act)
        res_word = ''.join(stacks[2])
        if len(actions) > min_length:
            print("It can be shorter.")
            return False
        if res_word == end:
            return True
        else:
            print("The result anagram is wrong.")
            return False

    assert check_solution(checkio, "rice-cire", 5), "rice-cire"
    assert check_solution(checkio, "tort-trot", 4), "tort-trot"
    assert check_solution(checkio, "hello-holle", 14), "hello-holle"
    assert check_solution(checkio, "anagram-mragana", 8), "anagram-mragana"
    assert check_solution(checkio, "mirror-mirorr", 25), "mirror-mirorr"