# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# szukamy cyklu w dagu, jesli istnieje to zwracamy False


prerequisities = [[1,2], [2,3], [6,4], [10,8]]


def canFinish(n, pre):

    # Detect cycle using DFS. Color nodes as per the following:
    # White - Node is never visited
    # Grey - Node is being visited (i.e. it's adjacent nodes are being visited). If we land on a grey node in our DFS; there's a cycle.
    # Black - Node and all it's adjacent vertices are visited.

    # Create adjancency list
    graph = [[] for _ in range(n)]
    for u, v in pre:
        graph[v].append(u)

    visited = [False] * n           # Start with all "white"s           # nieodwiedzony

    def is_cyclic(u):
        if visited[u] is None:
            return True

        if visited[u] is True:
            return False

        visited[u] = None           # Set color of node to "grey"       # odwiedzony, ale nieprzetworzony
        for v in graph[u]:
            if is_cyclic(v):
                return True

        visited[u] = True           # Set color of node to "black"      # przetworzony

        return False

    for u in range(n):
        if is_cyclic(v):
            return False

    return True