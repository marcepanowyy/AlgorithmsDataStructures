# Rozważmy słowa x[0]x[1] · · · x[n − 1] oraz y[0]y[1] · · · y[n − 1] składające się z małych
# liter alfabetu łacińskiego. Takie dwa słowa są t-anagramem (dla t ∈ {0, . . . , n − 1}), jeśli każdej literze
# pierwszego słowa można przypisać taką samą literę drugiego, znajdującą się na pozycji różniącej
# się o najwyżej t, tak że każda litera drugiego słowa jest przypisana dokładnie jednej literze słowa
# pierwszego.

# Proszę zaimplementować funkcję:

# def tanagram(x, y, t):
# ...

# która sprawdza czy słowa x i y są t-anagramami i zwraca True jeśli tak a False w przeciwnym razie.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową
# i pamięciową użytego algorytmu.

# Przykład. Słowa ”kotomysz” oraz ”tokmysoz” są 3-anagramami, ale nie są 2-anagramami:

# 0 1 2 3 4 5 6 7     0 1 2 3 4 5 6 7 - nr litery w słowie
# 2 1 0 6 3 4 5 7     2 1 0 4 5 6 3 7 - nr litery przypisanej w drugim słowie
# k o t o m y s z     t o k m y s o z

from zad1testy import runtests

def counting_sort(tab):

    n = len(tab)
    C = [0] * 26
    B = [0] * n

    for i in range(n):
        C[tab[i][0]] += 1

    for i in range(1, 26):
        C[i] = C[i] + C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[tab[i][0]]-1] = tab[i]
        C[tab[i][0]] -= 1

    return B

def tanagram1(x, y, t):

    n = len(x)
    A, B = [], []

    for i in range(n):
        A.append([ord(x[i])-97, i])
        B.append([ord(y[i])-97, i])

    A = counting_sort(A)
    B = counting_sort(B)

    for i in range(n):
        if abs(A[i][1] - B[i][1]) > t:
            return False

    return True

# runtests(tanagram1)

# Martyna Paliwoda solution

from collections import deque

def tanagram2(x, y, t):

    positions = [deque() for _ in range(26)]

    for i, c in enumerate(y):
        positions[ord(c)-97].append(i)

    for i, c in enumerate(x):
        closest = positions[ord(c)-97].popleft()

        # print(f"closet {c} is on {closest}")

        if abs(closest - i) > t:
            return False

    return True

# runtests(tanagram2)