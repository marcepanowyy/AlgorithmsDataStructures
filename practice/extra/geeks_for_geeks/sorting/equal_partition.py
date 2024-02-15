# Partition Equal Subset Sum

# Given an array arr[] of size N, check if it can be partitioned into two
# parts such that the sum of elements in both parts is the same.

# x + x = sum(arr)

# szukamy podzbioru, ktory bedzie sie sumowal do sum // 2

# wybieramy liczbe albo ja odrzucamy

def equal_partition(arr):

    n = len(arr)
    target = sum(arr) // 2

    if target % 2 != 0: return False

    dp = [[False] * (target + 1) for _ in range(n+1)]

    for value in arr:
        dp[value][0] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]

# solution with sets

def canPartition(nums):

    if sum(nums) % 2 != 0:
        return False

    target = sum(nums) // 2
    sums = set()

    sums.add(0)

    for num in nums:

        sumsCopy = set()
        for s in sums:

            if s + num == target:
                return True

            sumsCopy.add(s)
            sumsCopy.add(s + num)

        sums = sumsCopy

    return False