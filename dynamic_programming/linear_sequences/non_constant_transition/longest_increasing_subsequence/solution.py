"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

def length_of_lis_recursive(nums):
    def lis_helper(prev_index, current_index):
        if current_index == len(nums):
            return 0
        taken = 0
        if prev_index == -1 or nums[current_index] > nums[prev_index]:
            taken = 1 + lis_helper(current_index, current_index + 1)
        not_taken = lis_helper(prev_index, current_index + 1)
        return max(taken, not_taken)
    
    return lis_helper(-1, 0)


def length_of_lis_top_down(nums):
    memo = {}
    
    def lis_helper(prev_index, current_index):
        if current_index == len(nums):
            return 0
        if (prev_index, current_index) in memo:
            return memo[(prev_index, current_index)]
        taken = 0
        if prev_index == -1 or nums[current_index] > nums[prev_index]:
            taken = 1 + lis_helper(current_index, current_index + 1)
        not_taken = lis_helper(prev_index, current_index + 1)
        memo[(prev_index, current_index)] = max(taken, not_taken)
        return memo[(prev_index, current_index)]
    
    return lis_helper(-1, 0)

def length_of_lis_bottom_up(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
