from queue import Queue

def bipartite(graph):           # dla listy sasiedztwa

    queue = Queue()
    visited = [False] * len(graph)
    map = [None] * len(graph)

    queue.put(0)
    visited[0] = True
    map[0] = 0

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                if map[u] == 0:
                    map[v] = 1
                else:
                    map[v] = 0

            if map[v] == map[u]:
                return False

    return map
