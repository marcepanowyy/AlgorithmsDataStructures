# podobne do SplitArrayMinLargestSum w leet_code/sorting tylko rezultatem jest minimum z podciagow a nie maksimum
# n**3 (gorsze od nlogn ktore bylo przy sorting)
# nie moj kod

def find_division(A: 'sequence of numbers to split', k: 'number of splits'):
    if k == 0: return 0

    n = len(A)
    inf = float('inf')
    F = [[0] * (k + 1) for _ in range(n)]

    # Fill the column for k = 1
    F[0][1] = A[0]
    for i in range(1, n):
        F[i][1] = F[i - 1][1] + A[i]

    # Sotore sums of values from 0 index to 'i' index
    S = [0] * n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]

    # Find the maximum value of the minimum split for each k value based
    # upon results for the previous subsequences and k values
    for t in range(2, k + 1):
        # We will consider all numbers up to a number at 'i' index (inclusive)
        for i in range(t - 1, n):
            # Loop over an index of the last number which will be included
            # in the first t - 1 splits
            for j in range(t - 2, i):
                F[i][t] = max(F[i][t], min(F[j][t - 1], S[i] - S[j]))

    print(*F, sep='\n')

    return F[n - 1][k]

A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3
# print(find_division(A, k))