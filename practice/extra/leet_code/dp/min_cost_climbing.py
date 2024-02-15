# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# f(0) = f(1) = min(T[0], T[1])
# f(i) = min(f(i-1)+T[i-1], f(i-2)+T[i-2])

def solution(cost):
    n = len(cost)
    min_cost = [float('inf')] * n
    min_first = min(cost[0], cost[1])
    min_cost[0] = min_cost[1] = min_first
    for i in range(2, n):
        min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i - 2] + cost[i-2])
    return min_cost[n]

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6

cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]
solution(cost2)