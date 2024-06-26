"""
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Example 2:
Input: m = 3, n = 2
Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:
1 <= m, n <= 100
"""

def unique_paths_with_obstacles(obstacle_grid):
    def helper(x, y):
        if x < 0 or y < 0 or obstacle_grid[x][y] == 1:
            return 0
        if x == 0 and y == 0:
            return 1
        return helper(x - 1, y) + helper(x, y - 1)

    m, n = len(obstacle_grid), len(obstacle_grid[0])
    return helper(m - 1, n - 1)

def unique_paths_with_obstacles_top_down(obstacle_grid):
    memo = {}

    def helper(x, y):
        if x < 0 or y < 0 or obstacle_grid[x][y] == 1:
            return 0
        if x == 0 and y == 0:
            return 1
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = helper(x - 1, y) + helper(x, y - 1)
        return memo[(x, y)]

    m, n = len(obstacle_grid), len(obstacle_grid[0])
    return helper(m - 1, n - 1)

def unique_paths_with_obstacles_bottom_up(obstacle_grid):
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]