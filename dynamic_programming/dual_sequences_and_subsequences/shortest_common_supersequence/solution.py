"""
https://leetcode.com/problems/shortest-common-supersequence/description/

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

def shortest_common_supersequence_recursive(str1: str, str2: str) -> str:
    def lcs_length(i, j):
        if i == 0 or j == 0:
            return 0
        if str1[i - 1] == str2[j - 1]:
            return 1 + lcs_length(i - 1, j - 1)
        else:
            return max(lcs_length(i - 1, j), lcs_length(i, j - 1))

    def scs_length(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if str1[i - 1] == str2[j - 1]:
            return 1 + scs_length(i - 1, j - 1)
        else:
            return 1 + min(scs_length(i - 1, j), scs_length(i, j - 1))

    m, n = len(str1), len(str2)
    lcs_len = lcs_length(m, n)
    scs_len = scs_length(m, n)
    return scs_len - lcs_len

def shortest_common_supersequence_top_down(str1: str, str2: str) -> str:
    memo = {}

    def lcs_length(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 or j == 0:
            return 0
        if str1[i - 1] == str2[j - 1]:
            memo[(i, j)] = 1 + lcs_length(i - 1, j - 1)
        else:
            memo[(i, j)] = max(lcs_length(i - 1, j), lcs_length(i, j - 1))
        return memo[(i, j)]

    def scs_length(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return j
        if j == 0:
            return i
        if str1[i - 1] == str2[j - 1]:
            memo[(i, j)] = 1 + scs_length(i - 1, j - 1)
        else:
            memo[(i, j)] = 1 + min(scs_length(i - 1, j), scs_length(i, j - 1))
        return memo[(i, j)]

    m, n = len(str1), len(str2)
    lcs_len = lcs_length(m, n)
    scs_len = scs_length(m, n)
    return scs_len - lcs_len

def shortest_common_supersequence_bottom_up(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)

    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Compute the length of the shortest common supersequence
    lcs_length = dp[m][n]
    scs_length = m + n - lcs_length

    return scs_length
