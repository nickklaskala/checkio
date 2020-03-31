#!/usr/bin/env checkio --domain=py run family-gifts

# Every Christmas in my family, each of us gives a present to only one other person.    To organize who should offer a gift to whom (I call it the chain of presents),    we introduced a few rules:
# 
# - There should be a single chain where every person in the family is present,
# - Couples should not give to one another,
# - Every person should give a gift to a different person than they had in previous years
# 
# So the problem would be to find and list the longest list of chains of presents.    For example in a family {a,b,c,d} with couples=({a,b},{c,d}): [[a,c,b,d],[a,d,b,c]].
# 
# You are given a set of family member names and a list of couples in this family.    Find the maximum number of chains with all family members.    Gift chains should be represented as a list of names wherei-th gives a    present toi+1-th and the last person in the list to the first.
# 
# Input:Names of family members as a set of strings.    Couple list as a tuple of sets with two strings in each.
# 
# Output:The longest list of gift chains as a list/tuple of    lists/tuples with strings.
# 
# Precondition:
# 
# 
# len(couples) <= 7
# 
# END_DESC

def find_chains(family, couples):
    return []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, family, couples, total):
        user_result = function(family.copy(), tuple(c.copy() for c in couples))
        if (not isinstance(user_result, (list, tuple)) or
                any(not isinstance(chain, (list, tuple)) for chain in user_result)):
            return False
        if len(user_result) < total:
            return False
        gifted = set()
        for chain in user_result:
            if set(chain) != family or len(chain) != len(family):
                return False
            for f, s in zip(chain, chain[1:] + [chain[0]]):
                if {f, s} in couples:
                    return False
                if (f, s) in gifted:
                    return False
                gifted.add((f, s))
        return True

    assert checker(find_chains, {'Gary', 'Jeanette', 'Hollie'},
                   ({'Gary', 'Jeanette'},), 0), "Three of us"
    assert checker(find_chains, {'Curtis', 'Lee', 'Rachel', 'Javier'},
                   ({'Rachel', 'Javier'}, {'Curtis', 'Lee'}), 2), "Pairs"
    assert checker(find_chains, {'Philip', 'Sondra', 'Mary', 'Selena', 'Eric', 'Phyllis'},
                   ({'Philip', 'Sondra'}, {'Eric', 'Mary'}), 4), "Pairs and Singles"