#!/usr/bin/env checkio --domain=py run yaml-complex-structure

# The 4th task in the series of missions about the YAML format will be devoted to a complex structure.
# 
# An array element can be another array.
# 
# 
# - Alex
# -
#   - odessa
#   - dnipro
# - Li
# 
# [
#   "Alex", 
#   [
#     "odessa", 
#     "dnipro"
#   ], 
#   "Li"
# ]
# A dictionary can also be an element of an array.
# 
# 
# - 67
# -
#   name: Irv
#   game: Mario
# -
# - 56
# 
# 
# [
#   67, 
#   {
#     "game": "Mario", 
#     "name": "Irv"
#   }, 
#   null, 
#   56
# ]
# A dictionary element can be another dictionary.
# 
# 
# name: Alex
# study:
#   type: school
#   number: 78
# age: 14
# 
# {
#   "age": 14, 
#   "study": {
#     "type": "school", 
#     "number": 78
#   }, 
#   "name": "Alex"
# }
# An array can also be an element of a dictionary.
# 
# 
# name: Alex
# study:
#   - 89
#   - 89
#   - "Hell"
# age: 14
# 
# {
#   "age": 14, 
#   "study": [
#     89, 
#     89, 
#     "Hell"
#   ], 
#   "name": "Alex"
# }
# And, of course, data can have more than one nesting level.
# 
# 
# name: Alex
# study:
#   -
#     type: school
#     num: 89
#   -
#     type: school
#     num: 12
# age: 14
# 
# {
#   "age": 14, 
#   "study": [
#     {
#       "num": 89, 
#       "type": "school"
#     }, 
#     {
#       "num": 12, 
#       "type": "school"
#     }
#   ], 
#   "name": "Alex"
# }
# Input:Format string.
# 
# Output:An object.
# 
# Precondition:The YAML 1.2 standard is being used.
# 
# 
# END_DESC

def yaml(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]
    assert yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]
    assert yaml('- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5') == [1, 2, 3, 4, 5]
    assert yaml('-\n-\n-\n- 7') == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")