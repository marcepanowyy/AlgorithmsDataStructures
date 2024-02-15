import random

# Sortowanie kubełkowe - bucket sort

# Sortujemy tablicę n liczb pochodzących z rozkładu
# jednostajnego nad przedziałem [0,1)

# 0.42, 0.13, 0.07, 0.21, 0.91, 0.13, 0.37

# Tworzymy n kubełkow (kubelek - lista jednokier.)

# w naszym przypadku 7 kubelkow

# przedzialy to 1/n

# [0.15), [0.15, 0.30), ..., (0.90, 1)

# rozdzielam liczby do odpowiednich kubełków

# sortujemy kazdy kubelek osobno

# Sortujemy przez wybieranie/wstawianie

# kopiujemy kolejno liczby z kubełków do
# tablicy wyjściowej

# jak przydzielić liczbę do kubełka?
# jesli x nalezy do [0,1)
# to x laduje w kubelku podloga z x*n

# liczba kubelkow musi zalezec od rozmiaru danych
# i musi zalezec liniowo
# (najprostrza rzecz - tyle kubelkow co rozmiar tablicy)

# jesli spelnione zalozenia oczekiwany - O(n)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


def find_bucket(val, n, _min, _max):
    i = int((val - _min) / (_max - _min) * n)
    if i == n: i -= 1
    return i


def bucket_sort(A):

    n = len(A)
    _min, _max = min(A), max(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[find_bucket(A[i], n, _min, _max)].append(A[i])

    for i in range(n):
        insertion_sort(B[i])

    i = 0

    for j in range(n):
        for k in range(len(B[j])):
            A[i] = B[j][k]
            i += 1

    return A


A1 = [0, 100, 20, 80, 30, 60, 40, 50, 50]
# print(bucket_sort(A1))