# wykonujemy dfs, przetworzone wierzcholki dopisujemy na poczatek listy

def topological_sort1(G):  # reprezentacja macierzowa - DAG O(V+E)

    n = len(G)
    visited = [False] * n
    stack = []

    def DFS_visit(G, v):
        # nonlocal visited, stack
        visited[v] = True
        for i in range(n):
            if G[v][i] != 0 and not visited[i]:
                DFS_visit(G, i)
        stack.append(v)

    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    return stack

# G = [[0,1,1,0,0,0],[0,0,0,1,0,0],[0]*6, [0,0,0,0,1,1], [0]*6, [0]*6]
# print(topological_sort(G))


def topological_sort2(G: 'graph represented by adjacency lists'):

    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result

G1 = [[1,2], [2,4], [], [], [3,5,6], [], []]

# print(topological_sort2(G1))

G2 = [[1,2], [3,5], [3], [4], [], []]
# print(topological_sort2(G2))
