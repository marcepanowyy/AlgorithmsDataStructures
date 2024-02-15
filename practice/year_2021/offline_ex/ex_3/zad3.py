# takie jak zad.3 na kolosie I 2020/2021

# Paweł Konop

from zad3testy import runtests

# Zadanie offline 3.
# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego.  Rozkład ten mamy
# zadany jako k przedziałów [a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci,
# a liczba z przedziału (x ∈ [ai, bi]) jest losowana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić. Liczby ai, bi
# są liczbami naturalnymi ze zbioru  {1, . . . , N}. Proszę zaimplementować funkcję SortTab(T, P) sortująca podaną tablicę i zwracająca
# posortowaną tablicę jako wynik. Pierwszy argument to tablica do posortowania a drugi to opis przedziałów w postaci:
# P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.

# Na przykład dla wejścia:

# T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
# P = [(1, 5, 0.75) , (4, 8, 0.25)]

# po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:

# T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]

# Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
# zaproponowanego algorytmu.


from math import *

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

def SortTab(T, P):
    n = len(T)
    buckets = [[] for _ in range(n)]
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

runtests( SortTab )

