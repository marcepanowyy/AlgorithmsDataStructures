# Longest Increasing Path in a Matrix

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not
# move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

def lip(graph):

    n, m = len(graph), len(graph[0])

    dp = [[0] * m for _ in range(n)]
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(i, j):

        if not dp[i][j]:

            res = 1

            for ver, hor in moves:
                new_i = i + ver
                new_j = j + hor

                if 0 <= new_i < n and 0 <= new_j < m:
                    if graph[new_i][new_j] > graph[i][j]:
                        res = max(res, 1 + dfs(new_i, new_j))

            dp[i][j] = res

        return dp[i][j]

    res = 0

    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i, j))

    # print(*dp, sep="\n")
    return res


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(lip(matrix))