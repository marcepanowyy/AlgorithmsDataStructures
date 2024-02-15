# Egzamin 2019/2020 Termin I zad. 1

# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
# opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None.
# Przykład Dla tablicy

G0 = [[0,5,1,8,0,0,0],
      [5,0,0,1,0,8,0],
      [1,0,0,8,0,0,8],
      [8,1,8,0,5,0,1],
      [0,0,0,5,0,1,0],
      [0,8,0,0,1,0,5],
      [0,0,8,1,0,5,0]]

# funkcja islands(G1, 5, 2) powinna zwrócić wartość 13

def convert(G):

    n = len(G)
    new_G = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v]:
                new_G[u].append([v, G[u][v]])

    return new_G

from queue import PriorityQueue

def islands(G, s, t):

    G = convert(G)
    n = len(G)
    weights = [[float("inf")] * 3 for _ in range(n)] # weights[u][0] - doszlismy krawedzia 1, weights[u][1] - doszlismy z 5, weights[u][2] - doszlismy z 8
    pq = PriorityQueue()

    pq.put((0, s, None, 1))
    pq.put((0, s, None, 5))
    pq.put((0, s, None, 8))

    def edge_id(prev_edge):
        if prev_edge == 1: return 0
        if prev_edge == 5: return 1
        return 2

    while not pq.empty():
        min_w, u, parent, prev_edge = pq.get()

        if min_w < weights[u][edge_id(prev_edge)]:

            weights[u][edge_id(prev_edge)] = min_w

            for v, weight in G[u]:

                if weights[v][edge_id(weight)] == float("inf") and prev_edge != weight:
                    pq.put((weights[u][edge_id(prev_edge)] + weight, v, u, weight))

    return min(weights[t])

# print(islands(G1, 5, 2))


G1 = [[0, 1, 0, 0, 0, 8, 0], [1, 0, 5, 0, 0, 0, 0], [0, 5, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 8], [8, 0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 8, 5, 0]]
G2 = [[0, 1, 0, 0, 0, 1], [1, 0, 5, 0, 0, 5], [0, 5, 0, 5, 8, 1], [0, 0, 5, 0, 8, 0], [0, 0, 8, 8, 0, 1], [1, 5, 1, 0, 1, 0]]

# print(islands(G0, 2, 5)) # ok
# print(islands(G1, 0, 4)) # ok
# print(islands(G2, 0, 3)) # ok