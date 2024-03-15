"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase, and it takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. 

How many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2

Example 2:
    Input: n = 3
    Output: 3
"""

from typing import List

def climb_stairs_recursive(n: int) -> int:
    if n < 0:
        return 0
    
    if n == 0:
        return 1
    
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)

def climb_stairs_recursive_memo(n: int) -> int:
    
    memo = {}
    
    def climb(n: int) -> int:
        
        if n in memo:
            return memo[n]
        
        if n <= 2:
            return n
        
        result = climb(n - 1) + climb(n - 2)
        
        memo[n] = result
        
        return result
    
    return climb(n)

def climb_stairs_dp(n: int) -> int:
    
    if n <= 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    cache = [0 for i in range(n+1)]
    
    # base cases
    cache[0] = 0
    cache[1] = 1
    cache[2] = 2
    
    for i in range(3, n+1):
        cache[i] = cache[i - 1] + cache[i - 2]
        
    return cache[n]


assert climb_stairs_dp(-1) == 0
assert climb_stairs_dp(0) == 0
assert climb_stairs_dp(1) == 1
assert climb_stairs_dp(21) == 17711
assert climb_stairs_dp(45) == 1836311903