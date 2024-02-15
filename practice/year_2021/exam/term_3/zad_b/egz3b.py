from egz3btesty import runtests

from collections import deque

def BFS(L):
    n = len(L)
    visited = [[False] * n for _ in range(n)]
    d = deque([])
    visited[0][0] = True
    d.append([0,0])

    while d:
        row, col = d.popleft()





def maze( L ):

    # tu prosze wpisac wlasna implementacje

    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
