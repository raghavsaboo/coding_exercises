"""
https://leetcode.com/problems/count-number-of-teams/

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
"""
from typing import List


def count_teams_recursive(rating: List[int]) -> int:
    def count_helper(curr_index: int, prev_rating: int, team_size: int) -> int:
        if team_size == 3:
            return 1
        if curr_index == len(rating):
            return 0
        count = 0
        for next_index in range(curr_index + 1, len(rating)):
            if (rating[next_index] > prev_rating and team_size == 1) or (rating[next_index] < prev_rating and team_size == 2):
                count += count_helper(next_index, rating[next_index], team_size + 1)
        return count
    
    total_count = 0
    for i in range(len(rating) - 2):
        total_count += count_helper(i, rating[i], 1)
    return total_count

def count_teams_top_down(rating: List[int]) -> int:
    memo = {}
    
    def count_helper(curr_index: int, prev_rating: int, team_size: int) -> int:
        if team_size == 3:
            return 1
        if curr_index == len(rating):
            return 0
        if (curr_index, prev_rating, team_size) in memo:
            return memo[(curr_index, prev_rating, team_size)]
        count = 0
        for next_index in range(curr_index + 1, len(rating)):
            if (rating[next_index] > prev_rating and team_size == 1) or (rating[next_index] < prev_rating and team_size == 2):
                count += count_helper(next_index, rating[next_index], team_size + 1)
        memo[(curr_index, prev_rating, team_size)] = count
        return count
    
    total_count = 0
    for i in range(len(rating) - 2):
        total_count += count_helper(i, rating[i], 1)
    return total_count

def count_teams_bottom_up(rating: List[int]) -> int:
    n = len(rating)
    count = 0
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                    count += 1
                    
    return count
