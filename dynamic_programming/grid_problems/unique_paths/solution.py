"""
https://leetcode.com/problems/unique-paths-ii/description/

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""

def unique_paths_recursive(self, m: int, n: int) -> int:
    def count_paths(x: int, y: int) -> int:
        if x == m - 1 and y == n - 1:
            return 1
        if x >= m or y >= n:
            return 0
        return count_paths(x + 1, y) + count_paths(x, y + 1)
    
    return count_paths(0, 0)

def unique_paths_top_down(self, m: int, n: int) -> int:
    memo = {}
    
    def count_paths(x: int, y: int) -> int:
        if x == m - 1 and y == n - 1:
            return 1
        if x >= m or y >= n:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = count_paths(x + 1, y) + count_paths(x, y + 1)
        return memo[(x, y)]
    
    return count_paths(0, 0)

def unique_paths_bottom_up(self, m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]