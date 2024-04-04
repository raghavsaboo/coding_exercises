"""
https://leetcode.com/problems/distinct-subsequences/description/

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

def num_distinct_recursive(s, t):
    def helper(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if s[i] == t[j]:
            return helper(i + 1, j + 1) + helper(i + 1, j)
        else:
            return helper(i + 1, j)
    
    return helper(0, 0)

def num_distinct_top_down(s, t):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if s[i] == t[j]:
            memo[(i, j)] = helper(i + 1, j + 1) + helper(i + 1, j)
        else:
            memo[(i, j)] = helper(i + 1, j)
        return memo[(i, j)]
    
    return helper(0, 0)

def num_distinct_bottom_up(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][n] = 1
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]
    
    return dp[0][0]
