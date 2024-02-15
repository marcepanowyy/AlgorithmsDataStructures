# (Wymiana walut)
# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.

# Mamy tabelę kursów walut
# 1PLN -> 0.25 EUR
# 1 EUR -> 3.87 PLN
# 1 USD -> ...

# Prosze stwierdzić czy istnieje sekwencja transakcji, ktora
# pozwala uzyskac wiecej pieniedzy niz mielismy na wejsciu

# kazda krawedz owdwracamy i logarytmujemy, korzystamy z algorytmu Floyda-Warshalla

import copy
import math


def create_graph(K):
    n = 0
    for e in K:
        n = max(n, e[0], e[1])
    n += 1
    G = [[0] * n for _ in range(n)]
    for e in K:
        G[e[0]][e[1]] = math.log(e[2])
    return G


def floyd_warshall(G: 'graph represented by adjacency matrix'):
    n = len(G)
    inf = float('inf')

    # Create a copy of a graph as we have to have lengths
    # of edges stored at the beginning of an algorithm
    W = copy.deepcopy(G)

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    # Detect negative cycles (the same approach as in the
    # Bellman-Ford's algoritm)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = -inf

    return W

def can_rise(K):
    G = create_graph(K)
    W = floyd_warshall(G)
    n = len(G)
    for i in range(n):
        for j in range(n):
            if W[i][j] == float('-inf'):
                return True
    return False


PLN = 0
EUR = 1
USD = 2
YEN = 3

K = [(PLN, EUR, 4.51), (PLN, USD, 3.68), (PLN, YEN, 0.034),
     (EUR, PLN, 0.22), (EUR, USD, 0.82), (EUR, YEN, 0.0075),
     (USD, PLN, 0.27), (USD, EUR, 1.22), (USD, YEN, 0.0091),
     (YEN, PLN, 29.83), (YEN, EUR, 133,47), (YEN, USD, 109.62)]

print(can_rise(K))