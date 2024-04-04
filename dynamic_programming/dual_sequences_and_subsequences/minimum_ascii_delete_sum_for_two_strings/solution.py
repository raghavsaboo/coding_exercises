"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 
Constraints:
1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
"""

def minimum_delete_sum_recursive(s1, s2):
    def helper(i, j):
        if i == len(s1):
            return sum(ord(ch) for ch in s2[j:])
        if j == len(s2):
            return sum(ord(ch) for ch in s1[i:])
        if s1[i] == s2[j]:
            return helper(i + 1, j + 1)
        else:
            return min(ord(s1[i]) + helper(i + 1, j), ord(s2[j]) + helper(i, j + 1))
    
    return helper(0, 0)

def minimum_delete_sum_top_down(s1, s2):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(s1):
            return sum(ord(ch) for ch in s2[j:])
        if j == len(s2):
            return sum(ord(ch) for ch in s1[i:])
        if s1[i] == s2[j]:
            memo[(i, j)] = helper(i + 1, j + 1)
        else:
            memo[(i, j)] = min(ord(s1[i]) + helper(i + 1, j), ord(s2[j]) + helper(i, j + 1))
        return memo[(i, j)]
    
    return helper(0, 0)

def minimum_delete_sum_bottom_up(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + ord(s1[i])
    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + ord(s2[j])
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(ord(s1[i]) + dp[i + 1][j], ord(s2[j]) + dp[i][j + 1])
    
    return dp[0][0]
