"""
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

Example 1:
Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

Example 2:
Input: arr = [4,11]
Output: 44
 

Constraints:
2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 231).
"""

def mct_from_leaf_values_recursive(arr):
    def helper(left, right):
        if left == right:
            return 0
        min_cost = float('inf')
        for i in range(left, right):
            max_left = max(arr[left:i + 1])
            max_right = max(arr[i + 1:right + 1])
            min_cost = min(min_cost, max_left * max_right + helper(left, i) + helper(i + 1, right))
        return min_cost

    return helper(0, len(arr) - 1)


def mct_from_leaf_values_top_down(arr):
    memo = {}

    def helper(left, right):
        if left == right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]
        min_cost = float('inf')
        for i in range(left, right):
            max_left = max(arr[left:i + 1])
            max_right = max(arr[i + 1:right + 1])
            min_cost = min(min_cost, max_left * max_right + helper(left, i) + helper(i + 1, right))
        memo[(left, right)] = min_cost
        return min_cost

    return helper(0, len(arr) - 1)

def mct_from_leaf_values_bottom_up(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    max_leaf = [[0] * n for _ in range(n)]

    for i in range(n):
        max_leaf[i][i] = arr[i]
        for j in range(i + 1, n):
            max_leaf[i][j] = max(max_leaf[i][j - 1], arr[j])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max_leaf[i][k] * max_leaf[k + 1][j])

    return dp[0][n - 1]
