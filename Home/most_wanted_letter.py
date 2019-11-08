#!/usr/bin/env checkio --domain=py run most-wanted-letter

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