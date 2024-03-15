"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

from typing import List

def min_cost_climbing_stairs_recursive(cost: List[int]) -> int:
    
    def min_cost(index: int) -> int:
        
        if index >= cost:
            return 0
        
        return cost[index] + min(min_cost(index + 1), min_cost(index + 2))
    
    return min(min_cost(0), min_cost(1))

def min_cost_climbing_stairs_dp(cost: List[int]) -> int:
    n = len(cost)
    
    # base cases
    if n == 0:
        return 0
    
    if n == 1:
        return cost[0]
    
    cache = [0 for i in range(n+1)]
    
    cache[0], cache[1] = cost[0], cost[1]
    
    for i in range(2, n):
        cache[i] = min(cache[i-1], cache[i-2]) + cost[i]
        
    return min(cache[n-1], cache[n-2])

assert min_cost_climbing_stairs_dp([10, 15, 20]) == 15
assert min_cost_climbing_stairs_dp([1,100,1,1,1,100,1,1,100,1]) == 6