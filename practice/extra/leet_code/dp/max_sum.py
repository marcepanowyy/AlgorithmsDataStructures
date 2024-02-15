# Kedane's algorithm

# Maximum sum subarray problem

def Kedane(T):
    n = len(T)
    max_sum = [float("-inf")] * n
    max_sum[0] = T[0]
    for i in range(1, n):
        max_sum[i] = max(max_sum[i-1] + T[i], T[i])
    return max(max_sum)

T = [2, -2, 4, 14, -4, -6, -3, 30, 3, -4]
Kedane(T)