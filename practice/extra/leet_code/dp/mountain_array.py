# Minimum Number of Removals to Make Mountain Array

# lis

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Given an integer array nums, return the minimum number of elements to remove to make nums a mountain array.

# O(n**2) mozna zrobic O(nlogn)

def lis(arr):

    n = len(arr)
    dp1 = [1] * n          # longest increasing subsequence
    dp2 = [1] * n          # longest decreasing subsequence

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp1[i] < dp1[j] + 1:
                dp1[i] = dp1[j] + 1

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[i] and dp2[i] < dp2[j] + 1:
                dp2[i] = dp2[j] + 1

    return dp1, dp2

def moutain_removal(arr):

    n = len(arr)
    prefix, suffix = lis(arr)
    value = float("inf")

    for i in range(n):
        if prefix[i] > 1 and suffix[i] > 1:
            value = min(value, n - (prefix[i] + suffix[i] - 1))

    return value

# ALBO nlogn

from bisect import bisect_left

def helper(arr):

    longest, res = [], []

    for x in arr:
        if not res or longest[-1] < x:
            longest.append(x)
            res.append(len(longest))
        else:
            idx = bisect_left(longest, x)
            longest[idx] = x
            res.append(idx + 1)

    return res

def moutain_dew(arr):

    n, min_val = len(arr), float("inf")
    lis, lds = helper(arr), helper(arr[::-1])[::-1]

    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            min_val = min(min_val, n - (lis[i] + lds[i] - 1))

    return min_val

# lds = [9, 8, 1, 7, 6, 5, 4, 3, 2, 1]
# lis = [1, 1, 1, 2, 2, 2, 2, 2, 2, 1]

# arr1 = [1, 10, 12, 3, 5, 20, 10, 12, 15, 18, 20]
# arr2 = [2, 1, 1, 5, 6, 2, 3, 1]
# arr3 = [1, 3, 1]
# arr4 = [1,2,3,4,4,3,2,1]
# arr5 = [9,8,1,7,6,5,4,3,2,1]


