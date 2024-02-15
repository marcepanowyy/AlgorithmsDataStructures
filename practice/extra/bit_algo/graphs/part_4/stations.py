# Jak dojade (kurwa nie wiem jak)

# Dana jest tablica dwuwymiarowa G, przedstawiajaca macierz sasiedztwa skierowanego grafu
# wazonego, ktory odpowiada mapie drogowej (wagi przedstawiaja odleglosc, liczba -1 oznacza
# brak krawedzi). lecture niektorych wierzcholkach sa stacje paliw, podana jest ich lista P. Pelnego baku
# wystarczy na przejechanie odleglosci d. Wjezdzajac na stacje samochod zawsze jest tankowany do pelna.
# Prosze zaimplementowac funkcje jak_dojade(G, P, d, a, b), ktora szuka najkrotszej mozliwej trasy
# od wierzcholka a do wierzcholka b, jesli taka istnieje, i zwraca liste kolejnych odwiedzanych na trasie
# wierzcholkow (zakladamy, ze w a tez jest stacja paliw; samochod moze przejechac najwyzej odleglosc d
# bez zatankowania).

# Zaproponowana funkcja powinna byc jak najszybsza. Uzasadnij jej poprawnosc i
# oszacuj zlozonosc obliczeniowa

# Przyklad: dla tablic

G0 = [[-1, 6, -1, 5, 2],
      [-1, -1, 1, 2, -1],
      [-1, -1, -1, -1, -1],
      [-1, -1, 4, -1, -1],
      [-1, -1, 8, -1, -1]]

P0 = [0, 1, 3]

# funkcja jak_dojade(G, P, 5, 0, 2) powinna zwrocic [0,3,2]. Dla tych samych tablic
# funkcja jak_dojade(G, P, 6, 0, 2) powinna zwrocic [0,1,2], natomiast
# jak_dojade(G, P, 3, 0, 2) powinna zwrocic None

from queue import PriorityQueue

def create_fuel_map(P, n):

    map = [False] * n
    for v in P:
        map[v] = True
    return map

def get_solution(G, parents, t, fuel_left, map, d):
    if parents[t][fuel_left] == None: return [t]
    new_vertex = parents[t][fuel_left]
    new_fuel = ((fuel_left + G[new_vertex][t]) if not map[new_vertex] else d)
    return [t] + get_solution(G, parents, new_vertex, new_fuel, map, d)


def jak_dojade(G, P, d, s, t):

    n = len(G)
    map = create_fuel_map(P, n)
    pq = PriorityQueue()
    weights = [[float("inf")] * (d+1) for _ in range(n)]
    parents = [[None] * (d+1) for _ in range(n)]
    pq.put((0, s, None, d))

    while not pq.empty():
        min_w, u, parent, fuel_left = pq.get()
        if map[u]: fuel_left = d

        if min_w < weights[u][fuel_left]:
            weights[u][fuel_left] = min_w
            parents[u][fuel_left] = parent

            for v in range(n):
                if G[u][v] != -1 and fuel_left - G[u][v] >= 0:
                    pq.put((weights[u][fuel_left] + G[u][v], v, u, fuel_left - G[u][v]))

    fuel_left = -1
    min_cost = float("inf")

    for i in range(d+1):
        if weights[t][i] < min_cost:
            min_cost = weights[t][i]
            fuel_left = i

    if min_cost == float("inf"): return None

    return get_solution(G, parents, t, fuel_left, map, d)[::-1]


# print(jak_dojade(G0, P0, 5, 0, 2))
# print(jak_dojade(G0, P0, 6, 0, 2))
# print(jak_dojade(G0, P0, 3, 0, 2))

G1 = [[-1, -1, 8, -1, -1], [-1, -1, 5, -1, -1], [-1, -1, -1, 1, -1], [-1, -1, -1, -1, -1], [8, 5, -1, -1, -1]]
P1 = [0, 4]

# print(jak_dojade(G1, P1, 10, 4, 3))
