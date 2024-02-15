# Robot porusza się po dwuwymiarowym labiryncie i ma dotrzeć z pocycji A = (x[a], y[a]) na pozycję
# B = (x[b], y[b]). Robot może wykonać następujące ruchy:
#   1) ruch do przodu na kolejne pole,
#   2) obrót o 90 stopni zgodnie z ruchem wskazówek zegara,
#   3) obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.

# Obrót zajmuje robotowi 45 sekund. lecture trakcie ruchu do przodu robot się rozpędza i pokonanie pierwszego
# pola zajmuje 60 sekund, pokonanie drugiego 40 sekund, a kolejnych po 30 sekund na pole. Wykonanie
# obrotu zatrzymuje robota i następujące po nim ruchy do przodu ponownie go rozpędzają.

# Proszę zaimplementować funkcję:

# def robot(L, A, B):
#     ...

# która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B (lub zwraca
# None jeśli jest to niemożliwe).

# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.

# Labirynt. Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem
# składającym się z k kolumn. Pusty znak oznacza pole po którym robot może się poruszać, a znak ’X’
# oznacza ścianę labiryntu. Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.
# Pozycja robota. Początkowo robot znajduje się na pozycji A = (x[a], y[a]) i jest obrócony w prawo
# (tj. znajduje się w wierszu y[a] i kolumnie x[a], skierowany w stronę rosnących numerów kolumn).

from zad2testy import runtests
from queue import PriorityQueue

def robot(L, A, B):

    DP = [[[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]

    pq = PriorityQueue()
    pq.put((0, A[0], A[1], 0, 0))
    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]

    while not pq.empty():
        time, x, y, direction, idx = pq.get()
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        DP[y][x][direction][idx] = time
        pq.put((time + 45, x, y, (direction + 1) % 4, 0))
        pq.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        pq.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))

    return None

runtests(robot)