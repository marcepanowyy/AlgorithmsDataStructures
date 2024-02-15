# Distinct Subsequences

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# A string's subsequence is a new string formed from the original string by deleting some
# (can be none) of the characters without disturbing the remaining characters' relative positions.
# (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# The test cases are generated so that the answer fits on a 32-bit_algo signed integer.


def distinct(s, t):

    n, m = len(s), len(t)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):                         # jesli mamy otrzymac pusty napis t, to mozemy to zrobic na 1 sposob z napisu s (nie wybierajac zadnej nic)
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):

            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

            else:
                dp[i][j] = dp[i-1][j]

    # print(*dp, sep='\n')
    return dp[-1][-1]

s = "rabbbit"
t = "rabbit"

# [1, 0, 0, 0, 0, 0, 0]
# [1, 1, 0, 0, 0, 0, 0]
# [1, 1, 1, 0, 0, 0, 0]
# [1, 1, 1, 1, 0, 0, 0]
# [1, 1, 1, 2, 1, 0, 0]
# [1, 1, 1, 3, 3, 0, 0]
# [1, 1, 1, 3, 3, 3, 0]
# [1, 1, 1, 3, 3, 3, 3]

print(distinct(s, t))

