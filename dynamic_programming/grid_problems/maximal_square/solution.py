"""
https://leetcode.com/problems/maximal-square/description/

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

def maximal_square_recursive(matrix):
    def helper(i, j):
        if i == 0 or j == 0:
            return int(matrix[i][j])
        if matrix[i][j] == '0':
            return 0
        return min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1)) + 1

    max_side = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                max_side = max(max_side, helper(i, j))
    
    return max_side * max_side

def maximal_square_top_down(matrix):
    memo = {}

    def helper(i, j):
        if i == 0 or j == 0:
            return int(matrix[i][j])
        if (i, j) in memo:
            return memo[(i, j)]
        if matrix[i][j] == '0':
            return 0
        memo[(i, j)] = min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1)) + 1
        return memo[(i, j)]

    max_side = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                max_side = max(max_side, helper(i, j))
    
    return max_side * max_side

def maximal_square_bottom_up(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    max_side = 0
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side


"""
Time Complexity: O(m * n) as we iterate through each cell of the matrix once
Space Complexity: O(1) due to inplace modification
"""