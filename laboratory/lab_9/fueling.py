# Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden
# litr paliwa na jeden kilometr trasy. lecture baku mieści się dokładnie D litrów paliwa. Trasa jest reprezentowana
# jako graf, gdzie wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w
# kilometrach (przedstawioną jako liczba naturalna). lecture każdym wierzchołku jest stacja benzynowa, z daną ceną
# za litr paliwa. Proszę podać algorytm znajdujący trasę z punktu A do punktu B o najmniejszym koszcie.

from queue import PriorityQueue

# G - graph represented by adjacency matrix
# C - array of fuel prices on the stations
# d - capacity of a fuel tank
# fuel - initial amount of fuel
# s - start vertex
# t - end vertex

def dijkstra(G, C, d, fuel, s, t):
     n = len(G)
     inf = float('inf')
     W = [[inf] * (d + 1) for _ in range(n)]
     P = [[None] * (d + 1) for _ in range(n)]
     pq = PriorityQueue()
     pq.put((0, fuel, 0, s, None))

     end_fuel = None

     while not pq.empty():

          min_cost, fuel, prev_fuel, u, parent = pq.get()

          if min_cost < W[u][fuel]:
               W[u][fuel] = min_cost
               P[u][fuel] = (parent, prev_fuel)

               if u == t:
                    end_fuel = fuel
                    break

               for v, dist in G[u]:
                    for refueled in range(max(0, dist - fuel), d - fuel + 1):
                         new_fuel = fuel + refueled

                         if W[v][new_fuel] == inf:
                              pq.put((min_cost + refueled * C[u], new_fuel - dist, fuel, v, u))

     return (W, P, end_fuel) if end_fuel is not None else (None,) * 3


def get_path(P, end_fuel, t):
     path = [t]

     entry = P[t][end_fuel]
     while True:
          print(entry)
          t, fuel = entry
          if t is None: break
          path.append(t)
          entry = P[t][fuel]

     path.reverse()
     return path


def cheapest_travel(G, C, d, fuel, s, t):

     W, P, end_fuel = dijkstra(G, C, d, fuel, s, t)
     # print(*lecture, sep='\n')
     return (W[t][end_fuel], get_path(P, end_fuel, t)) if W else (None,) * 2

G = [[[1,6], [4,3], [3,8]],
     [[0,6], [2,5]],
     [[1,5], [6,2], [8,3]],
     [[0,8], [4,1], [5,4]],
     [[0,3], [3,1], [6,4]],
     [[3,4], [7,1]],
     [[2,2], [4,4], [7,2], [8,1]],
     [[5,1], [6,2], [8,5]],
     [[2,3], [6,1], [7,5]]]

T = [10, 20, 100, 4, 2, 6, 20, 1, 2]

print(cheapest_travel(G, T, 10, 0, 0, 7))
