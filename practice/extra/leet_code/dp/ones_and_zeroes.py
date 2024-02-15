# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.

# strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

# f(i,j) - maksymalna licznosc podzbioru zawierajaca co najwyzej 'i' zer oraz 'j' jedynek

def count(str):
    n = len(str)
    zeroes = 0
    for i in range(n):
        if str[i] == '0':
            zeroes += 1
    return zeroes, n - zeroes

def zeroes_onesTD(T, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]   # rows - zeroes, columns - ones
    for s in T:
        zeroes, ones = count(s)
        for z in range(m, zeroes-1, -1):
            for o in range(n, ones-1, -1):
                dp[z][o] = max(dp[z][o], 1 + dp[z-zeroes][o-ones])

    # actual_zeroes = m
    # actual_ones = n
    # while actual_zeroes - 1 >= 0 and dp[actual_zeroes][actual_ones] == dp[actual_zeroes-1][actual_ones]:
    #     actual_zeroes -= 1
    # while actual_ones - 1 >= 0 and dp[actual_zeroes][actual_ones] == dp[actual_zeroes][actual_ones-1]:
    #     actual_ones -= 1

    print(dp[m][n])
    return dp[m][n]


strs1 = ["10", "0001", "111001", "1", "0"]
zeroes_onesTD(strs1, 5, 3)

strs2 = ['111', '1', '0101', '0', '0101']
# zeroes_onesTD(strs2, 5, 5)

# weird stuff going on in here :C



