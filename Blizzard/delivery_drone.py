#!/usr/bin/env checkio --domain=py run delivery-drone

# Nowadays the drones are working in transportation. (Delivery drone(Wikipedia))Let's make a plan to ensure the efficient drone movement.
# 
# The input value is a list of integers.One or more numbers of this list represent the existence of the package(s) to be transported and its destination.You have to return the shortest moving distance for the drone to complete all transportation as an integer.
# 
# Note:The drone is initially at position 0 (far-left position).The drone can carry only one package at a time.You can drop the package only at the destination point.You aren't forced to pick up the package at the destination point.The dronereturnsto position 0.
# END_DESC

from typing import List


def delivery_drone(orders: List[int]) -> int:

    return 0


if __name__ == '__main__':
    assert delivery_drone([0, 2, 0]) == 4
    assert delivery_drone([0, 0, 1, 2]) == 6
    assert delivery_drone([0, 2, 4, 0, 1, 0, 5]) == 12
    print('The local tests are done. Click on "Check" for more real tests.')