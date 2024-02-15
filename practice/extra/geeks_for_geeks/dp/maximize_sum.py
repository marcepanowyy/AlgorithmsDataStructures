# Maximize sum of topmost elements of S stacks by popping at most N elements

# Given S stacks of length M, the task is to maximize the sum of elements at the top of
# each stack by popping at most N elements.

# Input: N = 3, stacks = [5, 1, 4, 8, 9]
# Output: 8

# Input: N = 2, stacks = [[2, 6, 4, 5], [1, 6, 15, 10]]
# Output: 17

# Input N = 10, stacks = [[8, 9, 3, 1, 4],
#                         [2, 7, 6, 3, 4],
#                         [1, 7, 1, 7, 19]]
# Output: 29 (remove 4 elements from stack nr 1, remove 2 elements from stack nr 2, remove 4 elements from stack nr 3)

from copy import deepcopy

def pop_elements(S, N):

    n = len(S)
    k = len(S[0])
    arr = deepcopy(S)

    for i in range(n):
        arr[i].append(0)

    dp = [[0] * (N + 1) for _ in range(n)]

    for j in range(min(N, k)):
        dp[0][j] = arr[0][j]

    for i in range(1, n):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j]
            for t in range(min(k, j)+1):
                a = dp[i-1][j-t]
                b = arr[i][t]
                dp[i][j] = max(dp[i][j], dp[i-1][j-t] + arr[i][t])

    print(*dp, sep="\n")
    print("max sum removing", N, "elements from stacks is", dp[n-1][N])
    return dp[n-1][N]

S1, N1 = [[8, 9, 3, 1, 4], [2, 7, 6, 3, 4], [1, 7, 1, 7, 19]], 10

S2, N2 = [[12, 7, 4, 3], [2, 7, 4, 5]], 4

S3, N3 = [[12, 7, 4, 3], [2, 7, 4, 5], [1, 1, 1, 1]], 12


# pop_elements(S1, N1)
# pop_elements(S2, N2)
pop_elements(S3, N3)
print("powinno byc 0 XD")



