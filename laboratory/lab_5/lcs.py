# Mamy dane dwie tablice A[n] i B[m]. Nalezy znalezc
# dlugosc ich najdluzszego wspolnego podciagu


# longest common subsequence

# f(i, j) = 1 + f(i-1, j-1) when A[i] == B[j]
# f(i, j) = max(f(i-1, j), f(i, j-1))


def LCS(A, B):
    if not A or not B: return 0
    n = len(A)
    m = len(B)
    F = [[0] * m for _ in range(n)]

    F[0][0] = int(A[0] == B[0])
    # Fill the first row (compare the first value of the array A
    # with all the values from the B array)
    for j in range(1, m):
        if F[0][j - 1] or A[0] == B[j]:
            F[0][j] = 1
    # Fill the first column (compare the first value of the array B
    # with all the values from the A array)
    for i in range(1, n):
        if F[i - 1][0] or B[0] == A[i]:
            F[i][0] = 1
    # Fill the remaining array based on values previously calculated
    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    print(*F, sep='\n')
    return F[n - 1][m - 1]