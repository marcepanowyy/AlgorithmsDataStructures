# dostajemy tablice n na m wypelniona wartosciami.
# Mamy za zadanie znalezc najdluzsza sciezke w tej tablicy
# (mozemy przechodzic na pola sasiadujace krawedziami), o rosnacych
# wartosciach (to znaczy, ze z pola o wartosci 3, moge przejsc na pola
# o wartosci wiekszej badz rownej 4).

def longest_path(A: 'matrix of values',
                 M: 'number of rows',
                 N: 'number of columns'):
    F = [[1] * N for _ in range(M)]

    def move(i, j):
        if F[i][j] > 1: return F[i][j]

        if i > 0 and A[i - 1][j] > A[i][j]:
            F[i][j] = max(F[i][j], move(i - 1, j) + 1)
        if i < M - 1 and A[i + 1][j] > A[i][j]:
            F[i][j] = max(F[i][j], move(i + 1, j) + 1)
        if j > 0 and A[i][j - 1] > A[i][j]:
            F[i][j] = max(F[i][j], move(i, j - 1) + 1)
        if j < N - 1 and A[i][j + 1] > A[i][j]:
            F[i][j] = max(F[i][j], move(i, j + 1) + 1)
        return F[i][j]

    max_length = 0
    res_coords = (0, 0)
    for i in range(M):
        for j in range(N):
            curr_length = move(i, j)
            if curr_length > max_length:
                max_length = curr_length
                res_coords = (i, j)

    return max_length, res_coords, F




