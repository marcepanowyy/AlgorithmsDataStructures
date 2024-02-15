# Minimum Cost To Make Two Strings Identical

# Given two strings X and Y, and two values costX and costY. We need to find minimum cost
# required to make the given two strings identical. We can delete characters from both the strings.
# The cost of deleting a character from string X is costX and from Y is costY. Cost of removing all
# characters from a string is same.

# Examples:

# Input :  X = "abcd", Y = "acdb", costX = 10, costY = 20.
# Output:  30
# For Making both strings identical we have to delete
# character 'b' from both the string, hence cost will
# be = 10 + 20 = 30.

# Input :  X = "ef", Y = "gh", costX = 10, costY = 20.
# Output:  60
# For making both strings identical, we have to delete 2-2
# characters from both the strings, hence cost will be =
#  10 + 10 + 20 + 20 = 60.

# longest common subsequence

def min_cost(X, Y, costX, costY):

    n1 = len(X)
    n2 = len(Y)
    dp = [[0] * n2 for _ in range(n1)]

    dp[0][0] = int(X[0] == Y[0])

    for j in range(1, n2):
        if dp[0][j-1] or X[0] == Y[j]:
            dp[0][j] = 1

    for i in range(1, n1):
        if dp[i-1][0] or X[i] == Y[0]:
            dp[i][0] = 1


    for i in range(1, n1):
        for j in range(1, n2):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # print(*dp, sep="\n")
    lcs = dp[-1][-1]
    cost = costX * (n1 - lcs) + costY * (n2 - lcs)
    print(cost)
    return cost

X1 = 'abcd'
Y1 = 'acdb'
costX1 = 10
costY1 = 20

X2 = "ef"
Y2 = "gh"
costX2 = 10
costY2 = 20

# min_cost(X1, Y1, costX1, costY1)
# min_cost(X2, Y2, costX2, costY2)
