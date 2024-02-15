def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key

A = [9, 6, 5, 4, 2, 1]
InsertionSort(A)
print(A)


