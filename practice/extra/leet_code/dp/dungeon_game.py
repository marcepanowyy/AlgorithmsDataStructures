# Dungeon Game

# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon.
# The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned
# in the top-left room and must fight his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health
# point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health
# upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that
# increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the
# bottom-right room where the princess is imprisoned.

# O(nm) bottom-up

def dungeon_game(dungeon):

    n = len(dungeon)  # rows
    m = len(dungeon[0])  # columns

    # dp = [[1] * n ] * m # this would be problematic because we are making duplicates and when dp[1][1] changes, dp[0][1] also changes
    # dp[i][j] means the minimum health needed to arrive bottom right, i.e., start from (i, j) to the bottom right
    # we start from bottom right because there are only two ways: rightward and downward,
    # we can reverse infer which step we should taken from the bottom right

    dp = [[1] * m for _ in range(n)]  # all the numbers init as 1 because the health at each cell should be at least 1, it cannot be 0 or negative

    if dungeon[n-1][m-1] < 0: dp[n-1][m-1] = -dungeon[n-1][m-1] + 1

    for i in range(n-2, -1, -1):
        if dungeon[i][m-1] < dp[i+1][m-1]: dp[i][m-1] = dp[i+1][m-1] - dungeon[i][m-1]

    for j in range(m-2, -1, -1):
        if dungeon[n-1][j] < dp[n-1][j+1]: dp[n-1][j] = dp[n-1][j+1] - dungeon[n-1][j]

    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):

                # pick the minimum health between downward or rightward step
                a, b = 1, 1

                # downward
                if dungeon[i][j] < dp[i + 1][j]:
                    a = dp[i+1][j] - dungeon[i][j]

                # rightward
                if dungeon[i][j] < dp[i][j + 1]:
                    b = dp[i][j + 1] - dungeon[i][j]

                dp[i][j] = min(a, b)

    return dp[0][0]

dungeon1 = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Expected: 7

dungeon2 = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
# Expected: 3

# print(dungeon_game(dungeon1))
# print(dungeon_game(dungeon2))
