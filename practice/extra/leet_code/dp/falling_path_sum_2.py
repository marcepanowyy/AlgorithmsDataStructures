# Minimum Falling Path Sum II

# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that
# no two elements chosen in adjacent rows are in the same column.


def falling_path2(grid):

    n = len(grid)
    m = len(grid[0])

    dp = [[0] * m for _ in range(n)]
    dp[0] = grid[0][:]

    for i in range(1, n):

        min_val, prev_min_val = float("inf"), float("inf")
        min_idx, prev_min_idx = None, None

        for j in range(m):

            if dp[i-1][j] < min_val:
                prev_min_val = min_val
                prev_min_idx = min_idx
                min_val = dp[i-1][j]
                min_idx = j

            elif dp[i-1][j] <= prev_min_val:
                prev_min_val = dp[i-1][j]
                prev_min_idx = j

        for j in range(m):
            if j == min_idx:
                dp[i][j] = grid[i][j] + dp[i-1][prev_min_idx]
            else:
                dp[i][j] = grid[i][j] + dp[i-1][min_idx]

    return min(dp[n-1])


grid1 = [[1,2,3],[4,5,6],[7,8,9]]
grid2 = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
grid3 = [[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]
grid4 = [[-2,-18,31,-10,-71,82,47,56,-14,42],[-95,3,65,-7,64,75,-51,97,-66,-28],[36,3,-62,38,15,51,-58,-90,-23,-63],[58,-26,-42,-66,21,99,-94,-95,-90,89],[83,-66,-42,-45,43,85,51,-86,65,-39],[56,9,9,95,-56,-77,-2,20,78,17],[78,-13,-55,55,-7,43,-98,-89,38,90],[32,44,-47,81,-1,-55,-5,16,-81,17],[-87,82,2,86,-88,-58,-91,-79,44,-9],[-96,-14,-52,-8,12,38,84,77,-51,52]]

