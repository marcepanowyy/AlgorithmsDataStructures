# [2pkt.] Zadanie 3.
# Szablon rozwiązania: zad3.py
# Dany jest zbiór przedziałów A = {(a0, b0), . . . , (an−1, bn−1)}. Proszę zaimplementować funkcję:
# def kintersect( A, k ):
# ...
# która wyznacza k przedziałów, których przecięcie jest jak najdłuższym przedziałem. Zbiór A jest
# reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k ≥ 1 oraz
# k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę numerów
# przedziałów, które należą do rozwiązania.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu.
# Przykład: Rozważmy listę przedziałóœ:
# A = [(0,4),(1,10),(6,7), (2,8)]
# Dla k = 3 wynikiem powinno być [0,1,3] (lub dowolna permutacja tej listy), co daje przedziały o
# przecięciu [2, 4], o długości 4 − 2 = 2.

def kintersect(A, k):
    n = len(A)
    longest = 0
    res_spans = []

    if k == 1:
        for i in range(n):
            if A[i][1] - A[i][0] > longest:
                longest = A[i][1] - A[i][0]
                res_spans = [i]
    else:
        for i in range(n):
            A[i] = A[i], i
        A.sort(key=lambda tup: tup[0][1], reverse=True)

        for i in range(n):
            spans = [A[i][1]]
            for j in range(n):
                if i == j or A[j][0][0] > A[i][0][0]: continue
                spans.append(A[j][1])
                if len(spans) == k: break

            if len(spans) < k: continue

            length = min(A[i][0][1], A[j][0][1]) - A[i][0][0]
            if length > longest:
                longest = length
                res_spans = spans

    return res_spans

A = [(10, 11), (9, 12), (8, 13), (7, 14), (6, 15)]
k = 3


# print(kintersect(A,k))

B = [(4,7), (8,12), (8,14), (9,20)]
print(kintersect(B, 2))

# 'res': 5,
# 'sol': [2, 3, 4]