"""
https://leetcode.com/problems/largest-sum-of-averages/description/

You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.

Example 1:
Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation: 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Example 2:
Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 104
1 <= k <= nums.length
"""

def largest_sum_of_averages_recursive(A, K):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    def average(start, end):
        return (prefix_sum[end] - prefix_sum[start]) / (end - start)

    def max_sum(start, k):
        if k == 1:
            return average(start, n)
        if start == n:
            return 0
        max_sum_result = 0
        for end in range(start + 1, n + 1):
            max_sum_result = max(max_sum_result, average(start, end) + max_sum(end, k - 1))
        return max_sum_result

    return max_sum(0, K)

def largest_sum_of_averages_top_down(A, K):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    memo = {}

    def average(start, end):
        return (prefix_sum[end] - prefix_sum[start]) / (end - start)

    def max_sum(start, k):
        if (start, k) in memo:
            return memo[(start, k)]
        if k == 1:
            return average(start, n)
        if start == n:
            return 0
        max_sum_result = 0
        for end in range(start + 1, n + 1):
            max_sum_result = max(max_sum_result, average(start, end) + max_sum(end, k - 1))
        memo[(start, k)] = max_sum_result
        return max_sum_result

    return max_sum(0, K)

def largest_sum_of_averages_bottom_up(A, K):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    dp = [[0] * (K + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = prefix_sum[i] / i

    for k in range(2, K + 1):
        for i in range(1, n + 1):
            for j in range(k - 1, i):
                dp[i][k] = max(dp[i][k], dp[j][k - 1] + (prefix_sum[i] - prefix_sum[j]) / (i - j))

    return dp[n][K]
