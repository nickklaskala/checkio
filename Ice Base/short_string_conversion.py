#!/usr/bin/env checkio --domain=py run short-string-conversion

# You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to transform line1 to line2?
# 
# Operations are:
# 
# Delete one letter from one of stringsInsert one letter into one of stringsReplace one of letters from one of strings with another letter
# 
# Input:two arguments, two strings.
# 
# Output:int, minimum number of operations.
# 
# 
# Precondition:0<= len(line)<100
# 
# 
# END_DESC

def steps_to_convert(line1, line2):
    return 0


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")