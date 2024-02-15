# Dany jest ważony graf nieskierowany reprezentowany przez macierz T o rozmiarach n × n (dla
# każdych i, j zachodzi T[i][j] = T[j][i]; wartość T[i][j] > 0 oznacza, że istnieje krawędź między
# wierzchołkiem i a wierzchołkiem j z wagą T[i][j]). Dana jest także liczba rzeczywista d. Każdy
# wierzchołek w G ma jeden z kolorów: zielony lub niebieski. Zaproponuj algorytm, który wyznacza
# największą liczbę naturalną l, taką że w grafie istnieje l par wierzchołków (p, q) ∈ V × V
# spełniających warunki:
#   1) q jest zielony, zaś p jest niebieski,
#   2) odległość między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest nie mniejsza niż d,
#   3) każdy wierzchołek występuje w co najwyżej jednej parze.
# Rozwiązanie należy zaimplementować w postaci funkcji:

# def BlueAndGreen(T, K, D):
#     ...

# która przyjmuje:
#   T: graf reprezentowany przez kwadratową macierz sąsiedztwa, gdzie wartość 0 oznacza brak krawędzi,
# a liczba większa od 0 przedstawia odległość pomiędzy wierzchołkami,
#   K: listę przedstawiającą kolory wierzchołków,
#   D: odległość o której mowa w warunku 2 opisu zadania.

# Funkcja powinna zwrócić liczbę l omawianą w treści zadania.
# Przykład. Dla argumentów:

# T = [
# [0, 1, 1, 0, 1],
# [1, 0, 0, 1, 0],
# [1, 0, 0, 0, 1],
# [0, 1, 0, 0, 1],
# [1, 0, 1, 1, 0],
# ]

# K = [’B’, ’B’, ’G’, ’G’, ’B’]
# D = 2
# wynikiem jest wartość 2.
#
# Maksymalny przepływ. Do treści zadania dostarczony jest plik zad3EK.py, w którym zaim-
# plementowany jest algorytm Edmondsa-Karpa obliczający maksymalny przepływ w grafie, w na-
# stępującej postaci:

# edmonds_karp(graph, source, sink)

from edmonds_karp import edmonds_karp
from floyd_warshall import floyd_warshall
from zad3testy import runtests

def BlueAndGreen(T, K, d):

    n = len(T)
    graph = [[0] * (n+2) for _ in range(n+2)]
    dist = floyd_warshall(T)

    for i in range(n):
        for j in range(n):
            if dist[i][j] >= d and dist[i][j] != float("inf") and K[i] == 'B' and K[j] == 'G':
                graph[i][j] = graph[j][n+1] = graph[n][i] = 1

    return edmonds_karp(graph, len(T), len(T) + 1)

# runtests(BlueAndGreen)

G = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

K = ['B', 'G', 'B', 'G', 'B', 'G', 'G', 'G', 'B', 'G', 'G']

d = 3

# print(BlueAndGreen(G, K, d))