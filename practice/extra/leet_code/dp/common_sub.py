# Shortest Common Supersequence

# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as
# subsequences. If there are multiple valid strings, return any of them.

# A string s is a subsequence of string t if deleting some number of characters from t
# (possibly 0) results in the string s.

def shortest_common_subsequence(s1, s2):

    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = int(s1[0] == s2[0])

    for i in range(1, n+1):
        for j in range(1, m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ans = ''

    while n > 0 and m > 0:

        if s1[n-1] == s2[m-1]:
            ans += s1[n-1]
            n -= 1
            m -= 1

        else:
            if dp[n-1][m] > dp[n][m-1]:
                ans += s1[n-1]
                n -= 1
            else:
                ans += s2[m-1]
                m -= 1

    while n > 0:
        ans += s1[n-1]
        n -= 1

    while m > 0:
        ans += s2[m-1]
        m -= 1

    return ans[::-1]

s1 = "bbbaaaba"
s2 = "bbababbb"
# Expected: 'bbbaaababbb'

# print(shortest_common_subsequence(s1, s2))