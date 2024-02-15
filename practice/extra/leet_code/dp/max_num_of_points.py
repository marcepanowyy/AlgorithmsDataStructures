# Maximum Number of Points with Cost

# You are given an m x n integer matrix points (0-indexed). Starting with 0 points,
# you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c)
# will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
# For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and
# (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

def maxPoints(points):

    n, m = len(points), len(points[0])

    for i in range(n-1):

        for j in range(1, m):
            points[i][j] = max(points[i][j], points[i][j-1] - 1)

        for j in range(m-2, -1, -1):
            points[i][j] = max(points[i][j], points[i][j+1] - 1)

        for j in range(m):
            points[i+1][j] += points[i][j]

    return max(points[n-1])


points1 = [[1,2,3],[1,5,1],[3,1,1]]
points2 = [[1,5],[2,3],[4,2]]

# print(maxPoints(points1))
# print(maxPoints(points2))