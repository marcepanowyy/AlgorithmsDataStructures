# Minimum jumps to reach end TUSHAR ROY

# [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
# T[i] - max steps you can forward from i index
# required output: 4 (from idx 0 to idx 1, from idx 1 to idx 4, from idx 4 to idx 5, from idx 5 to idx 9)

def get_solution(T, parents, i):
    if parents[i] == -1: return [0]
    return [i] + get_solution(T, parents, parents[i])

def jumps(T):

    n = len(T)
    min_jumps = [float("inf")] * n
    parents = [None] * n
    min_jumps[0] = 0
    parents[0] = -1

    for i in range(n):
        for j in range(i):
            if T[j] >= i-j and min_jumps[j]+1 < min_jumps[i]:
                min_jumps[i] = min_jumps[j]+1
                parents[i] = j

    res = get_solution(T, parents, n-1)
    print("minimum jumps:", min_jumps[n-1])
    print("jump indexes:", res[::-1])
    return min_jumps[n-1]

T = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
jumps(T)