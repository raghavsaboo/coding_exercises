"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def count_substrings_recursive(s: str) -> int:
    def is_palindrome(start, end):
        return all(s[start + i] == s[end - i] for i in range((end - start + 1) // 2))

    def count_palindromes(start):
        if start == len(s):
            return 0
        count = 0
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                count += 1
        return count + count_palindromes(start + 1)

    return count_palindromes(0)

def count_substrings_top_down(s: str) -> int:
    memo = {}

    def is_palindrome(start, end):
        return all(s[start + i] == s[end - i] for i in range((end - start + 1) // 2))

    def count_palindromes(start):
        if start == len(s):
            return 0
        if start in memo:
            return memo[start]
        count = 0
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                count += 1
        memo[start] = count + count_palindromes(start + 1)
        return memo[start]

    return count_palindromes(0)

def count_substrings_bottom_up(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    count = 0
    for i in range(n):
        dp[i][i] = 1
        count += 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1] == 1):
                dp[i][j] = 1
                count += 1

    return count
