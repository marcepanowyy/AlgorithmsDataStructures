# Maximum Sum of Two Non Overlapping Subarrays

# chore zadanie :)

# Given an integer array nums and two integers firstLen and secondLen, return the
# maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
# The array with length firstLen could occur before or after the array with length secondLen,
# but they have to be non-overlapping.
# A subarray is a contiguous part of an array.

def build_prefix_sum(T, l):
    n = len(T)
    prefix = [-1] * n
    prefix_sum = 0
    for i in range(l):
        prefix_sum += T[i]
        prefix[i] = prefix_sum
    for i in range(l, n):
        prefix[i] = prefix[i-1]+T[i]-T[i-l]

    max_prefix = [-1] * n
    max_prefix[0] = prefix[0]
    for i in range(1, n):
        max_prefix[i] = max(max_prefix[i-1], prefix[i])

    return max_prefix, prefix

def build_sufix_sum(T, l):
    n = len(T)
    sufix = [-1] * n
    sufix_sum = 0
    for i in range(l):
        sufix_sum += T[n-1-i]
        sufix[n-1-i] = sufix_sum
    for i in range(n-1-l, -1, -1):
        sufix[i] = sufix[i+1]+T[i]-T[i+l]

    max_sufix = [-1] * n
    max_sufix[n-1] = sufix[n-1]
    for i in range(n-2, -1, -1):
        max_sufix[i] = max(max_sufix[i+1], sufix[i])

    return max_sufix, sufix

def get_res(T, first_len, second_len):

    max_prefix1, prefix1 = build_prefix_sum(T, first_len)
    max_sufix1, sufix1 = build_sufix_sum(T, second_len)
    max_prefix2, prefix2 = build_prefix_sum(T, second_len)
    max_sufix2, sufix2 = build_sufix_sum(T, first_len)

    res = 0
    for i in range(1, len(T)):
        res = max(res, max_prefix1[i-1]+max_sufix1[i], max_prefix2[i-1]+max_sufix2[i])

    return res

