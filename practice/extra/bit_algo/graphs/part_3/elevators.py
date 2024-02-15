# Windy w drapaczu chmur
# Wieżowiec ma 100 pieter i n wind, nie ma natomiast schodów. Kazda winda
# posiada liste pięter, do których dojezdza i predkosc w sekundach na piętro.
# Jesteśmy na pietrze s, chcemy się dostac na piętro t. Ile minimalnie sekund
# musimy spędzić w windach, aby tam dotrzec?

from queue import PriorityQueue

def dijkstra(G, s, t):

    n = len(G)
    weights = [float("inf")] * n
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        min_w, u = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v))

    return weights

def create(elevators):

    G = [[] for _ in range(101)]

    for e, speed in elevators:
        n = len(e)
        for i in range(n):
            a = e[0:i]
            b = e[i+1:n]
            G[e[i]].append(e[0:e[i]], speed)
            G[e[i]].append(e[e[i]+2:n], speed)


elevators = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1)]
create(elevators)


def create_graph(elevators):
    # Find a number of floors
    n = 0
    for e in elevators:
        n = max(e[0])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in elevators:
        e[0].sort()
        for i in range(1, len(e[0])):
            G[e[0][i]].append((e[0][i - 1], (e[0][i] - e[0][i - 1]) * e[1]))
            G[e[0][i - 1]].append((e[0][i], (e[0][i] - e[0][i - 1]) * e[1]))
    return G


def min_time_in_elevators(elevators: 'array of tuples (floors connected, elevator speed)',
                          s: 'source', t: 'target'):
    G = create_graph(elevators)
    print(*G, sep='\n')
    # Run the Dijkstra's algorithm to find the minimum time
    return dijkstra(G, s, t)[t]

elevators = [([1, 2, 5], 1), ([0, 3, 5], 2), ([0, 3], 2), ([1, 2, 4], 3), ([3, 5], 1)]

print(min_time_in_elevators(elevators, 1, 3))