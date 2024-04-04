"""
https://leetcode.com/problems/longest-common-subsequence/description/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

def longest_common_subsequence_recursive(text1, text2):
    def helper(i, j):
        if i == -1 or j == -1:
            return 0
        if text1[i] == text2[j]:
            return helper(i - 1, j - 1) + 1
        else:
            return max(helper(i - 1, j), helper(i, j - 1))

    return helper(len(text1) - 1, len(text2) - 1)

def longest_common_subsequence_top_down(text1, text2):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == -1 or j == -1:
            return 0
        if text1[i] == text2[j]:
            memo[(i, j)] = helper(i - 1, j - 1) + 1
        else:
            memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))
        return memo[(i, j)]
    
    return helper(len(text1) - 1, len(text2) - 1)

def longest_common_subsequence_bottom_up(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]
