"""
https://leetcode.com/problems/partition-array-for-maximum-sum/description/

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
"""

def max_sum_after_partitioning_recursive(arr, k):
    def partition_helper(start):
        if start >= len(arr):
            return 0
        max_val = float('-inf')
        max_sum = float('-inf')
        for i in range(start, min(start + k, len(arr))):
            max_val = max(max_val, arr[i])
            current_sum = max_val * (i - start + 1) + partition_helper(i + 1)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    return partition_helper(0)

def max_sum_after_partitioning_top_down(arr, k):
    memo = {}
    
    def partition_helper(start):
        if start >= len(arr):
            return 0
        if start in memo:
            return memo[start]
        max_val = float('-inf')
        max_sum = float('-inf')
        for i in range(start, min(start + k, len(arr))):
            max_val = max(max_val, arr[i])
            current_sum = max_val * (i - start + 1) + partition_helper(i + 1)
            max_sum = max(max_sum, current_sum)
        memo[start] = max_sum
        return max_sum
    
    return partition_helper(0)

def max_sum_after_partitioning_bottom_up(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
    
    return dp[n]
