# [2pkt.] Zadanie 3.

# lecture roku 2050 Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Droga pomiędzy
# miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy. Maksymilian
# porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna wyposażona
# jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta B Maksymilian
# będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa), co każdorazowo wymaga
# zatrzymania cysterny. Niestety, droga jest niebezpieczna. Maksymilian musi więc tak zaplanować
# trasę, by zatrzymać się jak najmniej razy. Na szczęście cysterna Maksymiliana jest ogromna - po
# zatrzymaniu zawsze może zebrać całą ropę z plamy (w cysternie zmieściłaby się cała ropa na trasie).

# Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powinien się zatrzymać i
# zebrać ropę.
# Algorytm powinien być możliwe jak najszybszy i zużywać jak
# najmniej pamięci. Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.

# Dane wejściowe reprezentowane są jako dwuwymiarowa tablica liczb naturalnych T, w której wartość
# T[u][v] to objętość ropy na polu o współrzędnych (u, v) (objętość 0 oznacza brak ropy).
# Współrzędne u należą do zbioru {0, 1, . . . , n−1} a współrzędne v to zbioru {0, 1, . . . , m−1}.
# Miasto A znajduje się na polu (0, 0), zaś miasto B na polu (0, m − 1). Maksymilian porusza się jedynie po polach
# (0, 0), (0, 1), . . . (0, m − 1). Bok każdego pola ma długość 1 kilometra. Plamą ropy jest dowolny
# spójny obszar pól zawierających ropę. Dwa pola należą do spójnego obszaru jeśli mają wspólny
# bok lub są połączone sekwencją pól (zawierających ropę) o wspólnych bokach.
# Zakładamy, że początkowo cysterna jest pusta, ale pole (0, 0) jest częścią plamy ropy, którą można zebrać przed
# wyruszeniem w drogę. Zakładamy również, że zadanie posiada rozwiązanie, t.j. da się dojechać z
# miasta A do miasta B.

# Algorytm należy zaimplementować w funkcji:

# def plan(T):
# ...

# która przyjmuje tablicę z opisem zadania i zwraca listę współrzędnych v pól na których należy
# zatrzymać cysternę w celu zebrania ropy (cysterna porusza się po tylko polach (0, v), więc wystarczy
# zwrócić współrzędną v). Lista powinna być posortowana w kolejności postojów. Postój na polu (0, 0)
# również jest częścią rozwiązania.

from zad3testy import runtests
from queue import PriorityQueue

def bfs(T, n, m, curr_row, curr_col):
    if curr_col >=0 and curr_col <= m-1 and curr_row >= 0 and curr_row <= n-1 and T[curr_row][curr_col] > 0:
        res = T[curr_row][curr_col]
        T[curr_row][curr_col] = 0
        return res + bfs(T, n, m, curr_row + 1, curr_col) + bfs(T, n, m, curr_row, curr_col - 1) + bfs(T, n, m, curr_row, curr_col + 1) + bfs(T, n, m, curr_row - 1, curr_col)
    else:
        return 0

def plan(T):
    n = len(T)
    m = len(T[0])
    R = [0] * m
    res = [0]

    for i in range(m):
        R[i] = bfs(T, n, m, 0, i)

    radius = R[0]
    pointer = 1
    pq = PriorityQueue()

    if radius >= m - 1:
        return res

    while pointer != m-1:
        while pointer <= radius and pointer != m-1:
            if R[pointer] != 0:
                pq.put((-R[pointer], pointer))
            pointer += 1

        extra_range, index = pq.get()
        extra_range *= (-1)
        res.append(index)
        radius += extra_range
        if radius >= m-1:
            res.sort()
            return res

    return None

runtests(plan)


