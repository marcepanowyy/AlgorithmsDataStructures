# Non-negative Integers without Consecutive Ones

# Given a positive integer n, return the number of the integers in the range [0, n]
# whose binary representations do not contain consecutive ones.

# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.

# Input: n = 1
# Output: 2

def find_Intgers(n):
    b = str(bin(n))[2:]
    nbits = len(b)
    dp = [1] * (nbits)
    dp[1] = 2
    for i in range(2, nbits):
        dp[i] = dp[i-1] + dp[i-2]

    cnt = 0
    for i in range(nbits - 1):
        if b[i] == "1":
            cnt += dp[nbits - 2 - i]
        if i > 0 and b[i] == b[i - 1] == "1":
            return cnt
    if len(b) > 1 and b[nbits - 1] == b[nbits - 2] == "1":
        return cnt + 1
    return cnt + int(b[nbits - 1]) + 1



find_Intgers(33)
