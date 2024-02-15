# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9

# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4

# najmniejsza suma jaka mozemy uzyskac to max element z tablic
# najwieksza suma to suma wszystkich elementow w tablicy
# binary searchem szukamy sumy optymalnej

def can_split(mid, nums, m):
    n = len(nums)
    curr_sum, counter = 0, 1
    for i in range(n):
        curr_sum += nums[i]
        if curr_sum > mid:
            curr_sum = nums[i]
            counter += 1
        if counter > m: return False

    return True

def get_solution(nums, m, max_sum):
    res = [[] for _ in range(m)]
    n = len(nums)
    curr_sum = 0
    counter = 0
    for i in range(n):
        curr_sum += nums[i]
        if curr_sum <= max_sum: res[counter].append(nums[i])
        else:
            curr_sum = nums[i]
            res[counter+1].append(nums[i])
            counter += 1

    return res


def split_arr(nums, m):
    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = (left+right)//2
        if can_split(mid, nums, m):
            right = mid-1
        else:
            left = mid+1

    max_sum = left
    res = get_solution(nums, m, max_sum)
    print("max sum =", max_sum)
    print("split result:", res)

    return max_sum


nums = [10, 12, 3, 13, 4, 1, 0, 4, 3]
m = 4
# split_arr(nums, m)


nums1 = [10, 1, 5, 12, 0, 0, 5, 8, 3, 8, 4, 5, 2, 7, 21]
k = 6
split_arr(nums1, k)