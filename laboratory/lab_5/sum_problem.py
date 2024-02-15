# SUBSET SUM PROBLEM

# lecture problemie sumy podzbioru mamy dany ciag
# liczb A[0], A[1], ..., A[n-1] oraz liczbe p.
# Nalezy stwierdzic czy istnieje podciag sumujacy sie
# dokladnie do p

# f(i,j) = czy istnieje suma w podzbiorze {a0, ..., ai-1}
# o wartosci j

# f(0, 0) = p
# f(0, j) = False j > 0   # nie uzyskamy dodatniej sumy bez zadnej wartosci
# f(i, 0) = T
# f(i, j) = f(i-1, j) lub f(i-1, j-A[i-1]), gdzie j>=A[i-1]

def get_solution(sum_arr, T, i, p):
    if i == 0:
        if p-T[i] == 0: return [T[i]]
        else: return []
    if sum_arr[i-1][p]: return get_solution(sum_arr, T, i-1, p)
    else: return [T[i]] + get_solution(sum_arr, T, i-1, p-T[i])

def subset_sum_problem(T, p):
    n = len(T)
    sum_arr = [[False] * (p + 1) for _ in range(n)]
    for i in range(n):
        sum_arr[i][0] = True  # sume o wartosci 0 jestesmy w stanie zawsze otrzymac
    if T[0] <= p:
        sum_arr[0][T[0]] = True
    for num_idx in range(1, n):
        for value in range(1, p + 1):
            if sum_arr[num_idx - 1][value]:
                sum_arr[num_idx][value] = True
            elif value - T[num_idx] >= 0:
                if sum_arr[num_idx - 1][value - T[num_idx]]:
                    sum_arr[num_idx][value] = True

    if sum_arr[n-1][p] == False: return False

    return get_solution(sum_arr, T, n-1, p)[::-1]


T1 = [2, 3, 7, 8, 10]
p1 = 11

T2 = [2, 4, 5, 13, 7]
p2 = 18

# print(subset_sum_problem(T2, p2))