# Dana jest tablica zawierajaca n liczb z zakresu
# [0, ..., n^2-1]. Napisz algorytm, ktory posortuje taką
# tablicę w czasie O(n)


# z kazdej liczby robimy krotki
# k = (k//n, k % n)
#         k*n + k%n daje nam k

# sortujemy radix sortem te krotki
# zlozonosc O(2n)

# [0, ..., 24] (k = 5)

T = [12, 12, 9, 21, 2, 19, 24, 14, 2, 6, 9, 11, 15, 2, 15]


def make_array(T, n):
    length = len(T)
    for i in range(length):
        T[i] = (T[i]//n, T[i] % n)
    return T

# print(make_array(T, 5))

def radix_sort(arr):
    maximum = max(arr)
    div = 1
    while maximum // div != 0:
        counting_sort(arr, div)
        div *= 10
    return arr

def counting_sort(arr, div):
    n = len(arr)
    c_arr = [0] * 10
    output = [0] * n

    for i in range(n):
        index = (arr[i] // div) % 10
        c_arr[index] += 1

    for i in range(1, 10):
        c_arr[i] += c_arr[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // div) % 10
        output[c_arr[index] - 1] = arr[i]
        c_arr[index] -= 1

    for i in range(n):
        arr[i] = output[i]

# T = [45, 24, 12, 19, 24]
# print(radix_sort(T))

# ////////////////////////


# albo zamieniamy liczby na liczby o podstawie n i sortujemy counting sortem

def base_converter(T, base):
    n = len(T)
    for i in range(n):
        T[i] = (T[i]//base) * 10 + T[i] % base

def change_to_decimal(T, base):
    n = len(T)
    for i in range(n):
        T[i] = (T[i]//10) * base + T[i] % 10

def sorting(T, base):
    base_converter(T, base)
    radix_sort(T)
    change_to_decimal(T, base)
    return T

