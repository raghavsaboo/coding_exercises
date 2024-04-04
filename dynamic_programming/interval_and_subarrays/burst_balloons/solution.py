"""
https://leetcode.com/problems/burst-balloons/description/

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10
 

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

def max_coins_recursive(nums):
    def burst(left, right):
        if left + 1 == right:  # no balloons left to burst
            return 0
        max_coins = 0
        for i in range(left + 1, right):
            coins = nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right)
            max_coins = max(max_coins, coins)
        return max_coins

    nums = [1] + nums + [1]  # add boundary balloons with value 1
    return burst(0, len(nums) - 1)

def max_coins_top_down(nums):
    memo = {}

    def burst(left, right):
        if left + 1 == right:  # no balloons left to burst
            return 0
        if (left, right) in memo:
            return memo[(left, right)]
        max_coins = 0
        for i in range(left + 1, right):
            coins = nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right)
            max_coins = max(max_coins, coins)
        memo[(left, right)] = max_coins
        return max_coins

    nums = [1] + nums + [1]  # add boundary balloons with value 1
    return burst(0, len(nums) - 1)

def max_coins_bottom_up(nums):
    nums = [1] + nums + [1]  # add boundary balloons with value 1
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

    return dp[0][n - 1]
