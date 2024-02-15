# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego. Ten rozkład mamy zadany jako k przedziałów
# [a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci, a liczba z przedziału jest wybierana zgodnie z rozkładem jednostajnym.
# Przedziały mogą na siebie nachodzić, liczby ai, bi są liczbami naturalnymi ze zbioru {1, . . . , N}. Proszę zaimplementować funkcję SortTab(T,P) sortująca podaną tablicę.
# Pierwszy argument to tablica do posortowania a drugi to opis przedziałów w postaci:
# P = [(a1, b1, c1), (a2, b2, c2), . . ., (ak, bk, ck)].

# Na przykład dla wejścia:

P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]

# po wywołaniu SortTab(T,P) tablica T powinna być postaci:

# T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]

# Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
# zaproponowanego algorytmu.

# granice przedzialow sa liczbami naturalnymi
# ignorujemy czesc danych w tablicy P
# tworzymy prezdzialy jednostkowe, na kazdym przedziale jednostkowym wystepuje rozklad jednostajny


# O(n)

from math import *

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(T, P):
    max_ = ceil(max((T)))
    buckets = [[] for _ in range(max_+1)]
    interval = 1
    for elem in T:
        buckets[int(elem)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            T[i] = elem
            i += 1
    return T

# def bucket_sort(T, P):
#     n = len(T)
#     buckets = [[] for _ in range(n)]
#     interval = 1
#     for elem in T:
#         buckets[int(elem)].append(elem)
#     i = 0
#     for bucket in buckets:
#         bubble_sort(bucket)
#         for elem in bucket:
#             T[i] = elem
#             i += 1
#     return T

print(bucket_sort(T, P))
