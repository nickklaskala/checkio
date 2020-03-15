#!/usr/bin/env checkio --domain=py run network-loops

# A routing loop is a common problem with computer networks. Loops are virtually the same as cycles in graphs. For    this mission, we’ll learn how to find these cycles in a network.
# 
# A cycle consists of a sequence of nodes starting and ending on the same node without repetition and with each    consecutive node in the sequence connecting to each other in the network. The cycle length is the quantity of nodes    within the cycle. The length of cycle will always be greater than 2. You should find the largest cycle in a given    network, determine if we have multiple equal sized loops, then choose any one of them.
# 
# The nodes in the network are numbered and each connection is undirected. The length of the edges are not    substantial, so consider them to be of equal length. Some components of a network can be disconnected.
# 
# The network is represented as a sequence of connections. Each connection is described by the two two numbers    representing the connected nodes. The result should be given as a sequence of numbers which start and end with the    same number. If there is no cycle, then return an empty sequence.
# 
# 
# 
# For example this image will be described as: ((1,2),(2,3),(3,4),(4,5),(5,7),(7,6),(8,5),(8,4),(8,1),(1,5),(2,4)).    And the biggest loop have 6 nodes. It can be described as [1,2,3,4,5,8,1] (or [3,4,5,8,1,2,3]).
# 
# Input:Connection information as a tuple of tuples of integers.
# 
# Output:The largest cycle, or any one of the largest cycles as a list/tuple of integers.
# 
# Precondition:
# all([(n2, n1) in connections for n1, n2 in connections)
# 
# 
# 
# END_DESC

def find_cycle(connections):
    return []

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, connections, best_size):
        user_result = function(connections)
        if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
            print("You should return a list/tuple of integers.")
            return False
        if not best_size and user_result:
            print("Where did you find a cycle here?")
            return False
        if not best_size and not user_result:
            return True
        if len(user_result) < best_size + 1:
            print("You can find a better loop.")
            return False
        if user_result[0] != user_result[-1]:
            print("A cycle starts and ends in the same node.")
            return False
        if len(set(user_result)) != len(user_result) - 1:
            print("Repeat! Yellow card!")
            return False
        for n1, n2 in zip(user_result[:-1], user_result[1:]):
            if (n1, n2) not in connections and (n2, n1) not in connections:
                print("{}-{} is not exist".format(n1, n2))
                return False
        return True, "Ok"
    
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6),
                    (8, 5), (8, 4), (1, 5), (2, 4), (1, 8)), 6), "Example"
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 4), (1, 5), (2, 4)), 5), "Second"