# Mamy dany graf skierowany G = (V, E) oraz funkcję c: E → N opisującą przepustowość każdej krawędzi
# (liczbę jednostek towaru na godzinę, które mogą się przemieszczać krawędzią). Poza tym mamy dany zbiór
# wierzchołków-fabryk S = {s1, ..., sn} oraz zbiór wierzchołków-sklepów T = {t1, ..., tm}. Dla każdej
# fabryki s[i] znamy liczbę p[i] określającą ile jednostek towaru na godzinę fabryka może maksymalnie
# produkować. Jednocześnie dla każdego sklepu t[j] mamy liczbę q[j], która mówi ile jednostek towaru
# na godzinę musi do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się zapewnić,
# żeby do każdego sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga
# jednocześnie nie zmuszając żadnej fabryki do przekroczenia swoich możliwości produkcyjnych i nie
# przekraczając przepustowości żadnej z krawędzi.

# wystarczy zbudowac superzrodlo z odpowiednimi przepustowosciami do fabryk i superujscie
# od sklepow, a potem uzyc standardowego algorytmu


def create_graph(graph, factories, shops):

    n = len(graph)
    new_graph = [[0] * (n+2) for _ in range(n+2)]      # wierzcholek n jest superzrodlem, n+1 superujsciem
    estuary_val = 0

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u][v] = graph[u][v]

    for v, c in factories:
        new_graph[n][v] = c
    for v, c in shops:
        new_graph[v][n+1] = c
        estuary_val += c

    return new_graph, estuary_val

from edmonds_karp import edmonds_karp

def factories_and_shops(graph, factories, shops):

    n = len(graph)
    new_graph, estuary_value = create_graph(graph, factories, shops)
    max_flow = edmonds_karp(new_graph, n, n+1)

    if max_flow == estuary_value: return True
    return False

graph = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 6],
         [0, 0, 0, 0, 0, 0, 0]]

factories = [(1, 12), (0, 9)]
shops = [(4, 4), (6, 11)]

# print(factories_and_shops(graph, factories, shops))