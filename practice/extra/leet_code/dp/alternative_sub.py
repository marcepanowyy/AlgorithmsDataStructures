# Maximum Alternating Subsequence Sum

# The alternating sum of a 0-indexed array is defined as the sum of the elements at even indices
# minus the sum of the elements at odd indices.

# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# Given an array nums, return the maximum alternating sum of any subsequence of nums
# (after reindexing the elements of the subsequence).

# A subsequence of an array is a new array generated from the original array by deleting some
# elements (possibly none) without changing the remaining elements' relative order. For example,
# [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

# wybieramy liczbe, albo ja pomijamy

def alternating_sum(nums):

    n = len(nums)

    dp_odd, dp_even = [0] * n, [0] * n
    dp_even[0] = nums[0]
    max_even, max_odd = nums[0], 0

    for i in range(1, n):

        dp_odd[i] = max_even - nums[i]
        dp_even[i] = max_odd + nums[i]

        max_even = max(max_even, dp_even[i])
        max_odd = max(max_odd, dp_odd[i])

    return max(max(dp_even), max(dp_odd))

def max_alt_sum(nums):
    seq = [nums[0]]  # to store the sequence
    inc = True  # flag for increasing/decreasing
    for n1, n2 in zip(nums, nums[1:]):
        if (n2 > n1) == inc:  # same as if (n2 > n1 and inc == True) or (n2 <= 1 and inc == False)
            seq[-1] = n2  # we always choose the best option as noted above.
        else:
            # else, use it as new valid and flip the flag.
            seq.append(n2)
            inc = not inc

        # we always want odd-length seq because we exclude the last odd-index number.
    if len(seq) % 2 == 0: seq.pop()
    return sum(seq[::2]) - sum(seq[1::2])


nums1 = [4, 2, 5, 3]
nums2 = [5, 6, 7, 8]
nums3 = [6, 2, 1, 2, 4, 5]
nums4 = [6, 2, 1, 2, 4, 5]

# alternating_sum(nums4)
max_alt_sum(nums4)

