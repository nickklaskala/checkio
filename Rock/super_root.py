#!/usr/bin/env checkio --domain=py run super-root

# Square roots, cube roots, 4th roots... each are too boring for Nicola.    He needs to find the super root! With your help he will almost certainly find it.
# 
# The super root of a numberNis the numberx,    such thatxx=N.
# 
# The result should be accurate so thatxx≈ N±0.001.    OrN - 0.001 < xx< N + 0.001.
# 
# Input:A number (N) as an integer.
# 
# Output:The super root (x) as a float or an integer.
# 
# Precondition:
# 1 ≤ number ≤ 10 ** 10
# 
# 
# END_DESC

def super_root(number):
    return 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"