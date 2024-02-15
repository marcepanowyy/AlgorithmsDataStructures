# Dana jest szachownica o wymiarach n × n. Każde pole (i, j) ma koszt (liczbę ze zbioru {1, ..., 5})
# umieszczony w tablicy A (na polu A[j][i]). lecture lewym górnym rogu szachownicy stoi król, którego zadaniem
# jest przejsc do prawego dolnego rogu, przechodzac po polach o minmalnym sumarycznym koszcie. Prosze
# zaimplementowac funkcje kings_path(A), która oblicza koszt sciezki króla. Funkcja powinna byc mozliwie
# jak najszybsza.

from queue import PriorityQueue

def kings_path(T):
    n = len(T)
    queue = PriorityQueue()
    queue.put((T[0][0], 0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    cost = [[float("inf")] * n for _ in range(n)]
    cost[0][0] = T[0][0]
    while not queue.empty():
        dist, row, col = queue.get()
        visited[row][col] = True
        new_row = [row + 1, row + 1, row, row - 1, row - 1, row - 1, row, row + 1]
        new_col = [col, col + 1, col + 1, col + 1, col, col - 1, col - 1, col - 1]
        for i in range(8):
            if n > new_row[i] >= 0 and n > new_col[i] >= 0 and not visited[new_row[i]][new_col[i]] and cost[new_row[i]][new_col[i]] > cost[row][col] + T[new_row[i]][new_col[i]]:
                cost[new_row[i]][new_col[i]] = cost[row][col] + T[new_row[i]][new_col[i]]
                queue.put((T[new_row[i]][new_col[i]], new_row[i], new_col[i]))

    return cost[-1][-1]


T = [[3, 2, 1, 5],
     [2, 5, 4, 2],
     [1, 2, 5, 5],
     [2, 4, 2, 3]]

G1 = [[1,9,1,1,1,1,1,1,1],
     [1,9,1,9,9,9,9,9,1],
     [1,9,1,9,1,1,1,9,1],
     [1,1,1,9,1,9,1,1,1],
     [9,9,9,9,1,9,9,9,9],
     [9,9,9,9,1,1,1,1,1],
     [9,9,9,9,9,9,9,9,1],
     [9,9,9,9,9,9,9,9,1],
     [9,9,9,9,9,9,9,9,1]]

G2 = [[1,9,1,1,1,1,1,1,1],
     [1,0,1,9,9,9,9,9,1],
     [1,9,1,9,1,1,1,9,1],
     [1,1,1,0,1,9,1,1,1],
     [9,9,9,9,1,9,9,9,9],
     [9,9,9,9,1,1,1,1,1],
     [9,9,9,9,9,9,0,9,1],
     [9,9,9,9,9,9,9,0,1],
     [9,9,9,9,9,9,9,9,1]]

for i in range(len(G1)):
    for j in range(len(G1)):
        if G1[i][j] == 9:
            G1[i][j] = 100

print(*G1, sep='\n')

print(kings_path(G1))
print(kings_path(G2))