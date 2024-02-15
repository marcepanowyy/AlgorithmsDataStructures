from queue import PriorityQueue

## lista sąsiedztwa

graph = [[[1, 1], [2, 5]],
         [[0, 1], [4, 7], [3, 8], [2, 2]],
         [[0, 5], [1, 2], [3, 3]],
         [[2, 3], [1, 8], [4, 87]],
         [[1, 7], [3, 87]]]

def dijkstra1(graph, s):

    q = PriorityQueue()
    dist = [float('inf') for _ in range(len(graph))]
    counter = len(graph)
    q.put((0, s))

    while not q.empty() and counter > 0:
        d, v = q.get()
        if d < dist[v]:  # to się wykona tylko raz dla każdego wierzchołka
            counter -= 1
            dist[v] = d
            for edge in graph[v]:
                neighbor, edge_len = edge
                q.put((d + edge_len, neighbor))
    return dist


# print(dijkstra1(graph, 0))


def dijkstra2(G: 'graph represented by adjacency lists', s: 'source', t: 'target'):

    n = len(G)
    weights = [float("inf")] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent
            # Break a loop if we found a shortest path to the specified target
            # if u == t: break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == float("inf"):
                    pq.put((weights[u] + weight, v, u))

    # weights informuje nas ile min trzeba przebyc, zeby dostac sie do itego wierzcholka
    # parent pozwala odtworzyc sciezke

    return parents, weights


# G0 = [[[1,2],[2,50]],
#       [[0,2],[4,8]],
#       [[0,50],[3,50]],
#       [[2,50],[4, -10**6]],
#       [[1,8],[3,-10**6]]]
#
# dijkstra2(G0, 0, 4) # dijkstra nie dziala dla grafu o ujemnych krawedziach (TO BYL TEST) XD !!!

G1 = [[[1,2],[2,3],[3,10],[4,4]],
     [[0,2],[5,8]],
     [[0,3],[5,2],[7,9]],
     [[0,10],[6,1],[7,3]],
     [[0,4],[6,7]],
     [[1,8],[2,2],[6,4]],
     [[3,1],[4,7],[5,4],[7,9]],
     [[2,9],[3,3],[6,9]]]

# print(dijkstra2(G1,0,7))

G2 = [[[1,3],[2,8],[3,4]],
      [[0,3],[4,2],[5,4]],
      [[0,8],[5,1],[6,1]],
      [[0,4],[5,4]],
      [[1,2]],
      [[1,3],[3,4],[6,3]],
      [[2,1],[5,3]]]

# print(dijkstra2(G2,0,6))

#algorytm Dijkstry dla reprezentacji macierzowej

from queue import PriorityQueue

G = [[0,0,4,4],[0,0,3,3],[4,3,0,0],[4,3,0,0]]

from queue import PriorityQueue

def Dijkstra(G,s):

    n = len(G)
    pq = PriorityQueue()
    dist = [float("inf")] * n
    P = [None] * n

    def Relax(u, v):
        if dist[v] > dist[u] + G[u][v]:
            dist[v] = dist[u] + G[u][v]
            P[v] = u
            pq.put((dist[v], v))

    dist[s] = 0
    pq.put((dist[s], s))

    while not pq.empty():
        distance, u = pq.get()
        for i in range(n):
            if G[u][i] != None:
                Relax(u, i)

    return dist, P

# print(Dijkstra(G, 0))

