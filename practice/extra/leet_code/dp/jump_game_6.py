# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array.
# That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

# You want to reach the last index of the array (index n - 1).
# Your score is the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.

# Example 1:
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.


# Example 2:
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

# Example 3:
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0

nums1, k1 = [1, -1, -2, 4, -7, 3], 2

nums2, k2 = [10, -5, -2, 4, 0, 3], 3

nums3, k3 = [1, -5, -20, 4, -1, 3, -6, -3], 2

# O(n*k)

def max_result1(nums, k):

    n = len(nums)
    results = [float("-inf")] * n
    results[0] = nums[0]

    for i in range(n):
        for j in range(i+1, i+k+1):
            if j < n:
                results[j] = max(results[j], results[i] + nums[j])

    return results[n-1]


# dp[i] = max(dp[i-k+1]) + num[i]
#              i-k, ..., i-1

# O(nlogn)

from queue import PriorityQueue

def get_solution(parents, nums, index):
    if index < 0: return []
    return [nums[index]] + get_solution(parents, nums, parents[index])

def max_result2(nums, k):

    n = len(nums)
    dp = [float("-inf")] * n
    parents = [-1] * n
    pq = PriorityQueue()

    dp[0] = nums[0]
    pq.put((-nums[0], 0))

    for i in range(1, n):

        while not pq.empty():
            temp = pq.queue[0]
            if pq.queue[0][1] < i - k:
                pq.get()                        # usuwamy wartosci, ktore nie maja prawa byc w kolejce XD
            else:
                break

        value, index = pq.queue[0]
        value *= (-1)
        dp[i] = nums[i] + value
        parents[i] = index
        pq.put((-value-nums[i], i))

    res = get_solution(parents, nums, n-1)[::-1]         # dla duzych wynikow rekursja nie zadziala po max 999 wywolan, big sad
    print("maximum sum is", dp[n-1])
    print("numbers that created this sum:", res)
    return dp[n-1]

# max_result2(nums1, k1)
# max_result2(nums2, k2)
# max_result2(nums3, k3)



