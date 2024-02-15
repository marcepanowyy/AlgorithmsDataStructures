# Minimum Operations to Make the Array K-Increasing

# You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.

# The array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.

# For example, arr = [4, 1, 5, 2, 6, 2] is K-increasing for k = 2 because:
# arr[0] <= arr[2] (4 <= 5)
# arr[1] <= arr[3] (1 <= 2)
# arr[2] <= arr[4] (5 <= 6)
# arr[3] <= arr[5] (2 <= 2)
# However, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).
# In one operation, you can choose an index i and change arr[i] into any positive integer.

# Return the minimum number of operations required to make the array K-increasing for the given k

#        0  1  2  3  4  5  6  7   8   9
# arr = [4, 1, 5, 2, 6, 2, 8, 9, 11, 15]

# tablice dzielimy na k podtablic

# w kazdej podtablicy musi zachodzic sub_arr[i] <= sub_arr[i+1] dla kazdego i
# szukamy dlugosci LIS dla kazdej poddtablicy


from bisect import bisect_right

def lis(arr):

    longest, res, n = [], [], len(arr)

    for x in arr:
        if not res or longest[-1] <= x:
            longest.append(x)
            res.append(len(longest))
        else:
            idx = bisect_right(longest, x)           # bisect right (why? odpal debuggerem przyklad 4 z bisect left), bo moze byc <=
            longest[idx] = x
            res.append(idx + 1)

    return n - len(longest)


def k_increasing(arr, k):

    n, ans  = len(arr), 0
    groups = [[] for _ in range(k)]

    for i, num in enumerate(arr):
        groups[i % k] += [num]

    for group in groups:
        ans += lis(group)

    return ans

arr1 = [5, 4, 3, 2, 1]
k1 = 1
# Expected: 4

arr2 = [4, 1, 5, 2, 6, 2]
k2 = 2
# Expected: 0

arr3 = [4, 1, 5, 2, 6, 2, 8, 9, 11, 15]
k3 = 3
# Expected: 2

arr4 = [2, 2, 2, 2, 2, 1, 1, 4, 4, 3, 3, 3, 3, 3]
k4 = 1
# Expected: 4

# print(k_increasing(arr1, k1))
# print(k_increasing(arr2, k2))
# print(k_increasing(arr3, k3))
# print(k_increasing(arr4, k4))
