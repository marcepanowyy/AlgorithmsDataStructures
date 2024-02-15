### Implementacja bfs dla grafu w postaci macierzowej O(V**2)

from collections import deque

def bfs(G: 'graph represented using matrix'):

    n = len(G)
    visited = [False] * n
    d = deque([])

    for vertex in range(n):
        if visited[vertex]: continue
        d.append(vertex)
        visited[vertex] = True
        while d:
            u = d.popleft()
            for v in range(n):
                if G[u][v] and not visited[v]:
                    visited[v] = True
                    d.append(v)

G1 = [[0,1,0,0,0,0,0],
      [1,0,1,0,0,0,0],
      [0,1,0,1,1,0,0],
      [0,0,1,0,1,0,0],
      [0,0,1,1,0,1,0],
      [0,0,0,0,1,0,1],
      [0,0,0,0,0,1,0]]

# bfs(G1)