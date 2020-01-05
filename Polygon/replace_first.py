#!/usr/bin/env checkio --domain=py run replace-first

# In a given array the first element should become the last one. An empty array or array with only one element should stay the same.
# 
# 
# 
# Input:List.
# 
# Output:List.
# 
# 
# END_DESC

def replace_first(items: list) -> list:
    # your code here
    return items


if __name__ == '__main__':
    print("Example:")
    print(replace_first([1, 2, 3, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert replace_first([1]) == [1]
    assert replace_first([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")