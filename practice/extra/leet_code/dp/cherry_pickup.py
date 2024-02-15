# You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through, or
# -1 means the cell contains a thorn that blocks your way.
# Return the maximum number of cherries you can collect by following the rules below:

# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.


# dla uproszczenia algorytmu zauwazamy, ze
# przechodzac najpierw z (0,0) do (n-1, n-1) a potem z (n-1, n-1) do (0,0)
# wykonujemy te same operacje jakbysmy przeszli 2 razy z (0,0) do (n-1,n-1), wiec

# wyobrazmy sobie sytuacje, w ktorej dwie osoby wyruszaja z punktu (0,0)
# musza zebrac jak najwiecej wisni poruszajac sie tylko w dol i w prawo, konczac
# na (n-1, n-1)

# mozliwe pozycje:
# a1, b1, a2, b2

# [a1, b1] - pozycja pierwszej osoby
# [a2, b2] - pozycja drugiej osoby

# jesli dwie osoby wykonaja ruch w jednostce czasu, to suma pozycji wspolrzednych pierwszej osoby
# jest taka sama jak drugiej, stad

# a1 + b1 = a2 + b2    - zakladamy, ze poruszaja sie synchronicznie, robiac jeden ruch w jednej jednotce czasu
# # b2 = a1 + b1 - a2

# stad wystarczy trzymac w pamieci 3 wspolrzedne, wiec zlozonosc O(n**3)


# dp(a1, b1, a2) - maksymalna ilosc wisni, ktora mozemy zebrac majac
# pierwszego robota na pozycji (a1, b1) i drugiego na pozycji (a2, b2), gdzie b2 = a1 + b1 - a2

# O(n**3)


def cherry_pickup(grid):

    n = len(grid)
    dp = [[[float("-inf")] * n for _ in range(n)] for _ in range(n)]
    moves = [(1, 0), (0, 1)]

    dp[0][0][0] = grid[0][0]

    for a1 in range(n):
        for b1 in range(n):
            for a2 in range(n):
                b2 = a1 + b1 - a2
                if 0 <= b2 < n:
                    for down1, right1 in moves:
                        for down2, right2 in moves:

                            new_a1 = a1 + down1
                            new_b1 = b1 + right1
                            new_a2 = a2 + down2
                            new_b2 = b2 + right2

                            if 0 <= new_a1 < n and 0 <= new_b1 < n and 0 <= new_a2 < n and 0 <= new_b2 < n:

                                if grid[new_a1][new_b1] == -1 or grid[new_a2][new_b2] == -1 or grid[a1][b1] == -1 or grid[a2][b2] == -1: continue

                                if new_a1 == new_a2 and new_b1 == new_b2:
                                    dp[new_a1][new_b1][new_a2] = max(dp[new_a1][new_b1][new_a2], dp[a1][b1][a2] + grid[new_a1][new_b1])

                                else:
                                    dp[new_a1][new_b1][new_a2] = max(dp[new_a1][new_b1][new_a2], dp[a1][b1][a2] + grid[new_a1][new_b1] + grid[new_a2][new_b2])

    return dp[n-1][n-1][n-1] if dp[n-1][n-1][n-1] != float("-inf") else 0


grid1 = [[0,1,-1],[1,0,-1],[1,1,1]]
# Expected: 5

grid2 = [[1,1,1,1,0,0,0], [0,0,0,1,0,0,0], [0,0,0,1,0,0,1], [1,0,0,1,0,0,0], [0,0,0,1,0,0,0], [0,0,0,1,0,0,0], [0,0,0,1,1,1,1]]
# Expected: 15

grid3 = [[1,-1,-1,-1,-1],[1,0,1,-1,-1],[0,-1,1,0,1],[1,0,1,1,0],[-1,-1,-1,1,1]]
# Expected: 10

grid4 = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Expected: 0

# print(cherry_pickup(grid1))
# print(cherry_pickup(grid2))
# print(cherry_pickup(grid3))
# print(cherry_pickup(grid4))