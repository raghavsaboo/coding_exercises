"""
https://leetcode.com/problems/strange-printer/description/

There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""

def strange_printer_recursive(s: str) -> int:
    def helper(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return helper(i, j - 1)
        min_operations = float('inf')
        for k in range(i, j):
            min_operations = min(min_operations, helper(i, k) + helper(k + 1, j))
        return min_operations

    return helper(0, len(s) - 1)

def strange_printer_top_down(s: str) -> int:
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            memo[(i, j)] = helper(i, j - 1)
        else:
            min_operations = float('inf')
            for k in range(i, j):
                min_operations = min(min_operations, helper(i, k) + helper(k + 1, j))
            memo[(i, j)] = min_operations
        return memo[(i, j)]

    return helper(0, len(s) - 1)

def strange_printer_bottom_up(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = length
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]
