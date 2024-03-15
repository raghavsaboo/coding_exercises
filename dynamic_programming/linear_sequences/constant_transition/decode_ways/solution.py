"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

def num_decodings_recursive(s: str) -> int:

    def num_decodings(s: str, i: int):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        
        ways = num_decodings(s, i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
            ways += num_decodings(s, i + 2)
        
        return ways

    if not s:
        return 0
    return num_decodings(s, 0)

def num_decodings_memoization(s):
    memo = {}

    def num_decodings_recursive(s, i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in memo:
            return memo[i]
        
        ways = num_decodings_recursive(s, i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
            ways += num_decodings_recursive(s, i + 2)
        
        memo[i] = ways
        return ways

    return num_decodings_recursive(s, 0)

def num_decodings_bottom_up(s):
    if not s or s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
            dp[i] += dp[i - 2]

    return dp[-1]

assert num_decodings_bottom_up("226") == 3