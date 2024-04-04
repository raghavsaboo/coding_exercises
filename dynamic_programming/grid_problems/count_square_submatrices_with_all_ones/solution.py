"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices 
have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15

Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7

Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

def count_squares_recursive(matrix):
    def helper(i, j):
        if i == 0 or j == 0:
            return matrix[i][j]
        if matrix[i][j] == 0:
            return 0
        return min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1)) + 1

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += helper(i, j)
    return count

def count_squares_top_down(matrix):
    memo = {}

    def helper(i, j):
        if i == 0 or j == 0:
            return matrix[i][j]
        if matrix[i][j] == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1)) + 1
        return memo[(i, j)]

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += helper(i, j)
    return count

def count_squares_bottom_up(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if i > 0 and j > 0 and matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
            count += matrix[i][j]

    return count


"""
Time Complexity: O(m * n) as we iterate through each cell of the matrix once
Space Complexity: O(1) due to inplace modification
"""