"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List

def rob_recursive(nums: List[int]) -> int:
    
    def rob(nums: List[int], i: int) -> int:
        if i < 0:
            return 0
        return max(rob(nums, i - 2) + nums[i], rob(nums, i - 1))

    return rob(nums, len(nums) - 1)


def rob_memoization(nums):
    memo = {}

    def rob_recursive(nums, i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(rob_recursive(nums, i - 2) + nums[i], rob_recursive(nums, i - 1))
        return memo[i]

    return rob_recursive(nums, len(nums) - 1)


def rob_bottom_up(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


# Example usage:
nums = [2, 7, 9, 3, 1]
assert rob_recursive(nums) == 12
assert rob_memoization(nums) == 12
assert rob_bottom_up(nums) == 12