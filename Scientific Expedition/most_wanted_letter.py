#!/usr/bin/env checkio --domain=py run most-wanted-letter

# You are given a text, which contains different english letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

import string
def checkio(text):
	return max(string.ascii_lowercase, key=text.lower().count)

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [0, 0, 0,0,0,0,0,0]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2))



# '''
if __name__ == '__main__':
    print("Example:")
    print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Lorem ipsum dolor sit amet") == "m", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
# '''