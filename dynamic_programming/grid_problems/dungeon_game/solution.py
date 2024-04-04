"""
https://leetcode.com/problems/dungeon-game/description/

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1
 
Constraints:
m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""

def calculate_minimum_hp_recursive(dungeon):
    def helper(i, j):
        if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
            return max(1, 1 - dungeon[i][j])
        if i == len(dungeon) or j == len(dungeon[0]):
            return float('inf')
        return max(1, min(helper(i + 1, j), helper(i, j + 1)) - dungeon[i][j])
    
    return helper(0, 0)

def calculate_minimum_hp_top_down(dungeon):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
            return max(1, 1 - dungeon[i][j])
        if i == len(dungeon) or j == len(dungeon[0]):
            return float('inf')
        memo[(i, j)] = max(1, min(helper(i + 1, j), helper(i, j + 1)) - dungeon[i][j])
        return memo[(i, j)]
    
    return helper(0, 0)

def calculate_minimum_hp_bottom_up(dungeon):
    rows, cols = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
    dp[rows][cols - 1] = 1
    dp[rows - 1][cols] = 1
    
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
    
    return dp[0][0]
