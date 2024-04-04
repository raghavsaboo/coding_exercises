"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""

def min_path_sum(grid):
    def helper(x, y):
        if x < 0 or y < 0:
            return float('inf')
        if x == 0 and y == 0:
            return grid[0][0]
        return grid[x][y] + min(helper(x - 1, y), helper(x, y - 1))

    m, n = len(grid), len(grid[0])
    return helper(m - 1, n - 1)

def min_path_sum_top_down(grid):
    memo = {}

    def helper(x, y):
        if x < 0 or y < 0:
            return float('inf')
        if x == 0 and y == 0:
            return grid[0][0]
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = grid[x][y] + min(helper(x - 1, y), helper(x, y - 1))
        return memo[(x, y)]

    m, n = len(grid), len(grid[0])
    return helper(m - 1, n - 1)

def min_path_sum_bottom_up(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]
