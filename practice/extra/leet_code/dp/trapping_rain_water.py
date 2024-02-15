# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
# much water it can trap after raining.
# At any point i, the water that can be stored = minimum of (maximum height to left, maximum height to right ) - height at that point.


def trapping_water(height):

    n = len(height)
    L, R = [0] * n, [0] * n

    L[0] = height[0]
    R[n-1] = height[n-1]

    for i in range(1, n):
        L[i] = max(L[i-1], height[i])

    for i in range(n-2, -1, -1):
        R[i] = max(R[i+1], height[i])

    water = [0] * n

    for i in range(n):
        water[i] = min(R[i], L[i]) - height[i]

    return sum(water)

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trapping_water(height1))
