# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# f(i) - min steps to get to i position
# f(i) = min(f(i-1), nums[i])

# Input: nums = [2,3,1,1,4]
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Output: 2

# greedy solution O(n)

# rozwazmy tablice [2, 3, 1, 1, 4]
# z indeksu 0 mozemy skoczyc do indeksu 1 i 2
# [*2*, **3**, **1**, 1, 4] metoda podobna do bfs
# z indeksu 1 mozemy skoczyc do 2 ale to sie nie liczy bo juz jest odwiedzona
# mozemy tez skoczyc do 2 i 3 wiec robimy to itp.. (gwiazdki to kolorki)

def greedy_jump(nums):
    n = len(nums)
    res = 0
    l = r = 0
    while r < n-1:
        furthest = 0
        for i in range(l, r+1):
            furthest = max(furthest, i + nums[i])
        l = r+1
        r = furthest
        res += 1
    return res

# nums = [2,3,1,1,4]
# print(greedy_jump(nums))
