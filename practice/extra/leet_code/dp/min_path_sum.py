# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

def min_path(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    # m - rows
    # n - colums

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1], grid



grid1 = [[1,3,1],
        [1,5,1],
        [4,2,1]]

grid2 = [[1,2],[1,1]]

grid3 = [[1,2],
         [5,6],
         [1,1]]

min_path(grid1)
min_path(grid2)
print(min_path(grid3))