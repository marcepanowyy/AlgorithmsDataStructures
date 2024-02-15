# There is a row of n houses, where each house can be painted one of three colors: red, blue or green.
# The cost of painting each house with a certain colour is different. You have to paint all the houses
# such that no two adjacent houses have the same colour

# The cost of painting each house with a certain color is represented by an n * 3 cost matrix costs

# For example, costs[0][0] is the cost of painting house 0 with red, costs[1][2] is the cost of painting house
# 1 with green colour, and so on...

# Return the minimum cost to paint all houses

# Example 1:
# Input: costs[[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue
# Minimum cost: 2 + 5 + 3 = 10


#       red           blue            green
#  0    17             2               17
#  1  16+min(2,17)  16+min(17,17)   5+min(2,17)
#  2   ...            ...            ...

# f(i, colour) - minimalny koszt uzyty do pomalowanie do itego domu
# f(i, colour) = min(f(i-1, diff_colour1) + costs[i][colour], f(i-1, diff_colour2) + cost[i][colour])

def find_prev_min(i, res, colour):
    index = i-1
    if colour == 0:
        return min(res[index][1], res[index][2])
    if colour == 1:
        return min(res[index][0], res[index][2])
    if colour == 2:
        return min(res[index][0], res[index][1])
    return None


def paint_house(costs):
    n = len(costs)
    res = [[float("inf")] * 3 for _ in range(n)]
    for i in range(3):                                   # starting point
        res[0][i] = costs[0][i]
    for i in range(1, n):
        for colour in range(3):
                res[i][colour] = costs[i][colour] + find_prev_min(i, res, colour)
    return min(res[n-1])

costs = [[17,2,17],[16,16,5],[14,3,19]]
# print(paint_house(costs))