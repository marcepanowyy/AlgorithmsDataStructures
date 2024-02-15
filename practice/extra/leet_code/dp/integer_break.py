# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.


# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

def integerBreak(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    ans = [0] * (n + 1)
    ans[1] = 1
    ans[2] = 1
    ans[3] = 2

    for i in range(4, n + 1):
        ans[i] = max(2 * ans[i - 2], 3 * ans[i - 3], 2 * (i - 2), 3 * (i - 3))
    return ans[n]

integerBreak(10)