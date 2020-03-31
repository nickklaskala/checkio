#!/usr/bin/env checkio --domain=py run median-of-three

# 给你一个  整数列表 , 你需要创建并返回一个 列表 其中前两个元素要和输入列表一致, 从第三个元素开始，要取输入列表的该位置前三个数的中位数。
# 
# 等等...你不知道什么是‘中位数’? 那先来看看这个Checkio任务"Median".
# 
# 输入:整数列表。
# 
# 输出:整数列表。
# 
# The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import Iterable

def median_three(els: Iterable[int]) -> Iterable[int]:
    # your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")