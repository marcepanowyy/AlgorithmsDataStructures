# podobnie do floyda warshalla

def transitive_closure(graph):

    n = len(graph)
    RM = [[0] * n for _ in range(n)]    # reachability matrix

    for u in range(n):
        for v in range(n):
            if u == v:
                RM[u][v] = 1
            elif graph[u][v] == 1:
                RM[u][v] = 1

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if RM[u][v] == 1 or (RM[u][k] == 1 and RM[k][v] == 1):
                    RM[u][v] = 1
    return RM

graph = [[0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]

# print(*transitive_closure(graph), sep='\n')

