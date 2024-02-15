# Suma odleglosci

# Dana jest posortowana tablica A zawierajaca n liczb i celem jest
# wyznaczenie liczby x takiej, ze wartosc SUM from i=0 to i = n-1 |A[i]-x| jest minimalna.

# Prosze zaproponowac algorytm, uzasadnic jego poprawnosc oraz ocenic zlozonosc obliczeniowa

# median thing

from math import *

def min_sum(T):
    n = len(T)
    if n % 2 == 1: return T[n // 2]
    upper = n // 2
    lower = n // 2 - 1
    return (T[lower] + T[upper]) / 2

A = [1, 4, 7, 8]
B = [1, 4, 23, 88, 100, 412, 425, 500, 1000, 1202, 4014, 4444, 9999, 100000]

# print(min_sum(A))
# print(min_sum(B))
