"""
https://leetcode.com/problems/longest-palindromic-subsequence/description/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 
Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

def longest_palindromic_subsequence_recursive(s):
    def helper(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j]:
            return 2 + helper(i + 1, j - 1)
        else:
            return max(helper(i + 1, j), helper(i, j - 1))

    return helper(0, len(s) - 1)

def longest_palindromic_subsequence_top_down(s):
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j]:
            memo[(i, j)] = 2 + helper(i + 1, j - 1)
        else:
            memo[(i, j)] = max(helper(i + 1, j), helper(i, j - 1))
        return memo[(i, j)]

    return helper(0, len(s) - 1)

def longest_palindromic_subsequence_bottom_up(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and l == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
