"""
Given an integer `n`, return the least number of 
perfect square numbers that sum to `n`.

A perfect square is an integer that is a 
square of an integer, in other words, it is 
the product of some integer with itself. 

For example, 1, 4, 9, and 16 are perfect squares while
3 and 11 are not.

Example 1:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4
    
Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9
"""

def min_num_squares_recursive(n: int) -> int:
    
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    
    def min_num_squares(remaining: int) -> int:
        
        if remaining == 0:
            return 0
        
        min_count = float("inf")
        
        for square in squares:
            min_count = min(min_count, 1 + min_num_squares(remaining - square))
            
        return min_count
    
    return min_num_squares(n)


def min_num_squares_dp(n: int) -> int:
    
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    
    cache = [float("inf") for i in range(n+1)]
    
    # base case
    cache[0] = 0
    
    for target in range(1, n+1):
        
        for square in squares:
            
            if square > target:
                break
            
            cache[target] = min(cache[target], 1 + cache[target - square])
            
    return cache[n]

assert min_num_squares_dp(12) == 3
assert min_num_squares_dp(13) == 2 