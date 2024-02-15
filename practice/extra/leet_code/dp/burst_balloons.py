# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it
# represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1
# goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:
# Input: nums = [1,5]
# Output: 10

# f(i,j) - maksymalny zysk z pekniec od itego balonika do jtego balonika, uwzgledniajac
# ze miedzy indekssami i, j znajduje sie taki, ktory peka ostatni

# O(n**3) time cplx
# O(n**2) space cplx

from queue import PriorityQueue   # to get solution

def get_solution(last, profit):   # described later

    n = len(last)
    pq = PriorityQueue()
    res = []

    pq.put((-profit[0][n-1], 0, n-1))
    while not pq.empty():
        _, begin, end = pq.get()
        if begin <= end:
            balloon_idx = last[begin][end]
            res.append(balloon_idx)

        if begin < end:

            if balloon_idx - 1 >= 0:
                pq.put((-profit[begin][balloon_idx-1], begin, balloon_idx-1))
            if balloon_idx + 1 <= n-1:
                pq.put((-profit[balloon_idx+1][end], balloon_idx+1, end))

    return res[::-1]

def pop_ballons(nums):

    n = len(nums)
    profit = [[0] * n for _ in range(n)]                # profit[i][j] - max profit from popping balloons from index i to index j
    last = [[None] * n for _ in range(n)]               # last[i][j] - last popped balloon index in subarray [i,j]
    for i in range(n):
        profit[i][i] = (nums[i-1] if i != 0 else 1) * nums[i] * (nums[i+1] if i != n-1 else 1)
        last[i][i] = i

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i, j + 1):                                                              # k index balloon pops last
                left = (profit[i][k-1] if k != i else 0)                                           # left side profit (if k == i then there is nothing we can get from left side, otherwise we get profit from i to k-1)
                p = (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1)    # profit when k balloon bursts last in range [i,j] (if k'th balloon pops last, we get profit nums[i-1]*nums[k]*nums[j+1], we skip everything from index i to index j because everything here has already bursted besides k'th balloon)
                right = (profit[k+1][j] if k != j else 0)                                          # right side profit (if k == j then there is nothing we can get from right side, otherwise we get profit from k+1 to j)


                if profit[i][j] < (profit[i][k-1] if k != i else 0) + (profit[k+1][j] if k != j else 0) + (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1):
                    profit[i][j] = (profit[i][k-1] if k != i else 0) + (profit[k+1][j] if k != j else 0) + (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1)
                    last[i][j] = k                                                                 # update last popped balloon when profit is better


    res = get_solution(last, profit)                         # we get solution by putting in the priority queue subarrays that k balloon has divided
    print("popping order (from first to last):", res)        # e.g. consider nums2 = [9,5,13,1]. First, we look for last popped balloon in array 'last' from idex 0 to index 3
    print("max value of popping:", profit[0][n-1])           # last[0][3] is 2 (so last balloon that popped was with index '2'),
    return profit[0][n - 1]                                  # array is divided into [0,1] [3,3]. Now we look for index that gives us max profit from subarrays [0,1] and [3,3]
                                                             # we find max profit using Priority Queue, then we get next 'last balloon index' and so on



nums1 = [3, 1, 5, 8]
nums2 = [9, 5, 13, 1]
nums3 = [1, 5, 3, 20, 3, 5]

# pop_ballons(nums1)
# pop_ballons(nums2)
# pop_ballons(nums3)