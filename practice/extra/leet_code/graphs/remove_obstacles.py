# Minimum Obstacle Removal to Reach Corner

# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.

# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

# jesli grid[i][j] == 1, to krawedzie wchodzace do tego pola maja wartosc 1

# dp(i, j) - minimalna ilosc obiektow do usuniecia zeby dostac sie do pola (i, j)

# O(n*m)

from collections import deque

def obstacle_removal(grid):

    n, m = len(grid), len(grid[0])

    d = deque([])
    parents = [[None] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    moves = [(0,1), (1,0), (0,-1), (-1,0)]                  # (row, column)

    d.append((0, 0, 0))
    visited[0][0] = True

    while d:

        i, j, dist = d.popleft()

        if (i, j) == (n-1, m-1): return dist

        for add_row, add_column in moves:

            new_row = i + add_row
            new_column = j + add_column

            if 0 <= new_row < n and 0 <= new_column < m:

                if not visited[new_row][new_column]:

                    parents[new_row][new_column] = (i, j)
                    visited[new_row][new_column] = True

                    if grid[new_row][new_column]:
                        d.append((new_row, new_column, dist + 1))

                    else:
                        d.appendleft((new_row, new_column, dist))

    return None

# Latwe

grid1= [[0,1,1],[1,1,0],[1,1,0]]
# Expected: 2

grid2 = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# Expected: 0


# print(obstacle_removal(grid1))
# print(obstacle_removal(grid2))

