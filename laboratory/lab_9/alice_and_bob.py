# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi
# łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna).
# Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V, zamieniając się za kierownicą
# w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować
# algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała
# jak najmniej kilometrów.

G = [[[1,1], [2,3], [3,6]],
     [[0,1], [2,1], [4,3], [6,7]],
     [[0,3], [1,1], [4,8]],
     [[0,6], [5,1]],
     [[1,3], [2,8], [7,6]],
     [[3,1], [7,10]],
     [[1,7], [7,3], [8,8]],
     [[4,6], [5,10], [6,3], [9,10]],
     [[6,8], [9,6]],
     [[8,6], [7,10]]]


from queue import PriorityQueue

def dijkstra(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    n = len(G)
    inf = float('inf')
    weights = [[inf] * 2 for _ in range(n)]
    parents = [[None] * 2 for _ in range(n)]
    pq = PriorityQueue()
    # We will store in a pq queue tuples as follows:
    # (<Alice's distance>, <current vertex>, <parent vertex>, <flag indicating if
    # the last person who drives is Alice or Bob>)
    pq.put((0, s, None, 0))  # 0 - Alice starts
    pq.put((0, s, None, 1))  # 1 - Bob starts

    while not pq.empty():
        min_dist, u, parent, driver = pq.get()

        if min_dist < weights[u][driver]:
            weights[u][driver] = min_dist
            parents[u][driver] = (parent, int(not driver))
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                # Add a path only if there hasn't been the shortest path yet
                # If the last was Alice and there is no shortest path to the v
                # vertex on which the last driver was Bob
                if driver == 0 and weights[v][1] == inf:
                    # Now Bob drives, so Alice's distance isn't updated
                    pq.put((min_dist, v, u, 1))
                # The last driver was Bob and there is no shortest path to
                # the v vertex on which Alice drives last
                elif weights[v][0] == inf:
                    # Now Alice drives, so distance is updated
                    pq.put((min_dist + weight, v, u, 0))

    return weights

print(*dijkstra(G, 0, 4), sep="\n")


def get_path(parents, t, last_driver):
    path = []

    prev_driver = last_driver
    while t is not None:
        path.append(t)
        t, prev_driver = parents[t][prev_driver]

    path.reverse()

    return path, prev_driver


def drive_bus(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):
    # Let's say that we return ALice as there is noting to drive
    if s == t: return 'Alice', -1, []
    parents, weights = dijkstra(G, s, t)
    inf = float('inf')
    last_driver = 0 if weights[t][0] < inf else 1
    # Check if there is a path from s to t
    if weights[t][last_driver] == inf:
        return '', -1, []
    path, first_driver = get_path(parents, t, last_driver)
    return 'Alice' if not first_driver else 'Bob', weights[t][last_driver], path



# drive_bus(G, 0, 9)