def lis(A):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
            # if A[j] < A[i]:
            #     P[i] = j

    return F, P, max(P)

# T = [0, 1, 2, 4, 3]
#
T = [13, 7, 21, 42, 8, 2, 44, 53, 4]

# F, max, val,  P = (lis(T))
# print("tab A >> ", T)
# print("tab F >> ", F)
# print("max length = ", max)
# print("parent tab >>", P)

def maxindex(P, val):
    for i in range(len(P)):
        if P[i] == val:
            return i



def printsolution(A, P, i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i], end=" ")

# x, y, z = lis(T)
# printsolution(x, y, z)

# A = [4, 5, 1, 42, 5, 2, 1]
# index_max = max(range(len(A)), key = A.__getitem__)
# print(index_max)

# print("\n")
# printsolution(T, P, maxindex(P, val))

# def knapsackW(lecture, P, MaxW):
#     n = len(lecture)
#     F = [None] * n
#     F = [[0] * (MaxW+1) for i in range(n)]
#     for w in range(lecture[0], MaxW+1):
#         F[0][w] = P[0]
#
#     for i in range(1,n):
#         for w in range(1, MaxW+1):
#             F[i][w] = F[i-1][w]
#             if w >= lecture[i]:
#                 F[i][w] = max(F[i][w], F[i-1][w-lecture[i]]+P[i])
#     return F
#
# P = [10, 8, 4, 5, 3, 7]
# lecture = [4, 5, 12, 9, 1, 13]
# MaxW = 24

# F = knapsackW(lecture, P, MaxW)

# print(knapsackW(lecture, P, MaxW))
# for i in range(len(P)):
#     print(F[i])


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
MaxW = 24

def knapsack(W, P, MaxW):

    n = len(W)
    F = [[0]*(MaxW+1) for i in range(n)]

    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW+1):
            if w >= W[i]:
                F[i][w] = max(F[i-1][w], F[i-1][w-W[i]] + P[i])
            else:
                F[i][w] = F[i-1][w]

    return F


F = knapsack(W, P, MaxW)

# for i in range(len(F)):
#     print((F[i]))



# Mamy dany zestaw n odważników o masach danych liczbami naturalnymi. Napisz program, który sprawdza,
# czy zadany ciężar w można zważyć przy pomocy wagi dwuszalkowej (czyli odważniki mogą być po obu stronach wagi).
#
# def sum(lecture):
#     sum = 0
#     for i in range(len(lecture)):
#         sum += lecture[i]
#     return sum
#
# def rekur(lecture, w, p=0):
#     if w == 0:
#         return 1
#     if p == len(lecture):
#         return 0
#     if abs(sum(lecture) > abs(w)):
#         return rekur(lecture, w - lecture[p], p+1) or rekur(lecture, w, p+1) or rekur(lecture, w+lecture[p], p+1)
#     return 0
#
# lecture = [1, 2, 5, 10]
#
# print(rekur(lecture, 14))
#