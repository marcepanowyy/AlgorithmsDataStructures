# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the
# number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).

# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).

# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.

# When both robots stay in the same cell, only one takes the cherries.

# Both robots cannot move outside of the grid at any moment.

# Both robots should reach the bottom row in grid.


# O(n*m**2)

def cherry_pickup2(grid):

    n, m = len(grid), len(grid[0])
    positions = [-1, 0, 1]

    dp = [[[float("-inf")] * m for _ in range(m)] for _ in range(n)]

    # for a in range(m):                                               # myslalem ze zaczynamy z dowolnych pozycji XD
    #     for b in range(m):
    #         if a != b:
    #             dp[0][a][b] = grid[0][a] + grid[0][b]
    #         else:
    #             dp[0][a][b] = grid[0][a]

    dp[0][0][m-1] = grid[0][0] + grid[0][m-1]

    for i in range(1, n):
        for a in range(m):
            for b in range(m):
                for pos1 in positions:
                    for pos2 in positions:

                        new_pos1 = a + pos1
                        new_pos2 = b + pos2

                        if 0 <= new_pos1 < m and 0 <= new_pos2 < m:

                            if new_pos1 != new_pos2:
                                dp[i][new_pos1][new_pos2] = max(dp[i][new_pos1][new_pos2], dp[i-1][a][b] + grid[i][new_pos1] + grid[i][new_pos2])
                            else:
                                dp[i][new_pos1][new_pos2] = max(dp[i][new_pos1][new_pos2], dp[i-1][a][b] + grid[i][new_pos1])

    # print(*dp[n-1], sep='\n')
    return max(max(dp[n-1], key=max))


grid1 = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

grid2 = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

# print(cherry_pickup2(grid1))
# print(cherry_pickup2(grid2))

# Input:
grid3 = [[4,1,5,7,1],[6,0,4,6,4],[0,9,6,3,5]]
# Expected: 32

# Input:
grid4 = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Expected: 24

# print(cherry_pickup2(grid3))
# print(cherry_pickup2(grid4))

