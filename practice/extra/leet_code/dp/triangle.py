# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

def create_triangle(T):
    n = len(T)
    triangle = []
    for i in range(n):
        triangle.append([0]*(i+1))
    triangle[0][0] = T[0][0]
    for i in range(1, n):
        triangle[i][0] = triangle[i-1][0] + T[i][0]
        triangle[i][i] = triangle[i-1][i-1] + T[i][i]

    return triangle

def find_min_path_cost(T):
    n = len(T)
    if n <= 0: return None
    if n == 1: return T[0][0]
    res_triangle = create_triangle(T)
    for i in range(2, n):
        for j in range(1, len(T[i])-1):
            res_triangle[i][j] = min(res_triangle[i-1][j-1], res_triangle[i-1][j]) + T[i][j]

    return min(res_triangle[n-1])

# triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# x = find_min_path_cost(triangle)
# print(x)