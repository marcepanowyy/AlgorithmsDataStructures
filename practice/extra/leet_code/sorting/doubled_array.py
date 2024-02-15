# An integer array original is transformed into a doubled array changed by appending twice the value of every
# element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an
# empty array. The elements in original may be returned in any order.

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

# O(max(arr))

def doubled_array(arr):

    n, max_value = len(arr), max(arr)
    freq_arr, res = [0] * (max_value + 1), []
    m = len(freq_arr)                                               # counter - final legth arr

    for i in range(n):
        freq_arr[arr[i]] += 1

    while freq_arr[0] % 2 == 0 and freq_arr[0]:                     # 0 * 0 == 0, przypadek specjalny
        res.append(0)
        freq_arr[0] -= 2

    for i in range(m-1, 0, -1):                                     # zaczynamy od konca
        while i % 2 == 0 and freq_arr[i] and freq_arr[i//2]:
            freq_arr[i] -= 1
            freq_arr[i//2] -= 1
            res.append(i//2)

    if n == len(res) * 2:
        return res[::-1]
    return []

T = [4, 1, 2, 3, 4, 8, 2, 6, 10, 20]
# print(doubled_array(T))


# ze slownikiem O(nlogn)

from collections import Counter

def doubled_arr(arr):

    arr.sort()
    res = []
    counter = Counter(arr)

    for n in arr:
        if n not in counter:
            continue
        k = 2 * n
        if k in counter:
            res.append(n)
            counter[k] -= 1
            counter[n] -= 1
            if counter[n] == 0:
                del counter[n]
            if counter[k] == 0:
                del counter[k]
        else:
            return []

    if counter:
        return []
    else:
        return res
