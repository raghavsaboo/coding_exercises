"""
https://leetcode.com/problems/n-th-tribonacci-number/description/

The Tribonacci sequence T_n is defined as follows:

T_0 = 0, T_1 = 1, T_2 = 1, and T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0

Given `n` return the value of T_n

Example:
    Input: n = 4
    Output: 4

Example:
    Input: n = 25
    Output: 1389537
"""

def nth_tribonacci_dp(n: int) -> int:
    
    if n <= 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    cache = [0 for i in range(n+1)]
    
    # base cases
    cache[0], cache[1], cache[2] = 0, 1, 1
    
    for i in range(3, n+1):
        cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]
        
    return cache[n]


assert nth_tribonacci_dp(4) == 4
assert nth_tribonacci_dp(25) == 1389537