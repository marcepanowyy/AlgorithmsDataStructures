# You are given an integer array nums. You are initially positioned at the array's
# first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):

    n = len(nums)
    if n <= 1: return True

    max_reach = [0] * n
    max_reach[0] = nums[0]
    idx = 1

    while max_reach[idx-1] and idx < n:
        max_reach[idx] = max(max_reach[idx-1]-1, nums[idx])  
        idx += 1

    if max_reach[n-1]: return True
    return False


