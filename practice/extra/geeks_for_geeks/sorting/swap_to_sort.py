# Minimum number of swaps required to sort an array

# Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

# szukamy cykli

# dlugosc cyklu - 1 to minimalna ilosc zamian liczb ktore tworza wierzcholki

def swaps(arr):

    n, total = len(arr), 0
    checked = [False] * n
    connection = [-1] * n

    for i in range(n):
        arr[i] = [i, arr[i]]

    arr.sort(key=lambda x: x[1])

    for i in range(n):
        connection[i] = arr[i][0]              # connection[i] = k - pod indeksem i powinien byc indeks k

    for i in range(n):

        k = connection[i]

        if k == i or checked[i]:               # jesli indeks znajduje sie tam gdzie powininen lub jesli go juz sprawdzilismy
            checked[k] = True
            continue
        else:
            c = 0
            while not checked[k]:
                checked[k] = True
                k = connection[k]
                c += 1

        total += (c - 1)

    return total

arr1 = [3, 8, 20, 6, 15]
arr2 = [1, 4, 9, 2, 10, 12, 1, 15, 1, 2, 44]
arr3 = [2, 1, 0]
arr4 = [1, 8, 10, 9, 16]

# print(swaps(arr1))
# print(swaps(arr2))
# print(swaps(arr3))
# print(swaps(arr4))