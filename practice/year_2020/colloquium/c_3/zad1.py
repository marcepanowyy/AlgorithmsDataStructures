# [2pkt.] Zadanie 1.

# Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
# gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje
# te znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie (ale
# szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
# potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol
# i Maxa tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest
# jako graf nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym
# grafie). lecture jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z
# nich może się w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i
# Max nie mogą równocześnie poruszać się tą samą krawędzią (w przeciwnych kierunkach).
# Rozwiązanie należy zaimplementować w postaci funkcji:

# def keep_distance(M, x, y, d):
# ...

# która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
# kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi
# między wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami.
# lecture macierzy nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
# [(x, y), (u1, v1), (u2, v2), ..., (uk, vk), (y, x)]
# reprezentującą ścieżki Carol i Max. lecture powyższej liście element (ui, vi) oznacza, że Carol znajduje
# się w wierzchołku ui, zaś Max w wierzchołku vi. Można założyć, że rozwiązanie istnieje.
# Przykład. Dla argumentów:

# M = [[0, 1, 1, 0],
#      [1, 0, 0, 1],
#      [1, 0, 0, 1],
#      [0, 1, 1, 0]]

# x = 0
# y = 3
# d = 2

# wynikiem jest na przykład lista: [(0, 3), (1, 2), (3, 0) ]
# Podpowiedź. Proszę rozważyć nowy graf, być może z dużo większą liczbą wierzchołków niż graf
# wejściowy.


# Rozbijam graf w taki sposob ze w nowym grafie new_G pomiedzy kazda krawedzia powstaje d-1 nowych wierzcholkow.
# Dzieki temu w kazdym wierzcholku w nowym grafie bede mogl zapisac (przy pomocy algorytmu Dijkstry) czasy przejscia
# Carola tak jakby szedl przez graf sam. Nastepnie z drugiego konca rowniez uzywajac alg. Dijkstry i zagladajac
# do czasow przejscia Carola tym razem przechodzi Max pilnujac zeby zachowywac odleglosc co najmniej d.
# Jesli dotrze do punktu w ktorym odleglosc jest mniejsza niz d szuka innego mozliwego przejscia albo sie cofa.
# Jesli jest jakis punkt w ktorym moze poczekac to w nim czeka.

"""
lecture nowym grafie:

    Rozpatruje kazdy wierzcholek jako pare (u,v), ktora moze byc dowolna kombinacja wierzcholkow z pierwotnej
    macierzy

    Traktuje w takim grafie, ze istnieje krawedz miedzy (u,v) a (a,b) wtw, gdy istnieje krawedz (u,a) i (v,b)
    w grafie pierwotnym; dist(a,b) >= d; (u,v) != (b,a)

Uruchamiam bfsa na tym grafie, aby sprawdzic i znalezc odpowiednia sciezke, jesli takowa istnieje i da sie
dojechac do celu, zapisujac parentow w celu odzyskania rozwiazania (traktuje wagi krawedzi jako 1, bo nie wazne
jak szybko dojade, wazne czy dojade)

implementacyjnie wkladam do kolejki krotki (u,v), zeby nie musiec tworzyc calego nowego grafu

ALgorytmem floyda Warshalla obliczam doleglosci wszystkich:wszystkich aby sprawdzac to pozniej w czasie O(1)

Zlozonosc (V^4) - V^3 Floyd + V^4 bfs*|V'|, gdzie |V'| = |V|^2 """


from collections import deque
from floyd_warshall import floyd_warshall
from zad1testy import runtests

def keep_distance(graph, x, y, k):

    n = len(graph)
    S = floyd_warshall(graph)

    parents = [[None for _ in range(n)] for _ in range(n)]

    d = deque()
    d.append((x, y))

    while d:

        s, t = d.popleft()

        if s == y and t == x:
            break

        for u in range(n):

            # jesli jest polaczenie miedzy 'u' i 's' lub s == u

            if graph[s][u] or s == u:

                for v in range(n):

                    # jesli jest polaczenie miedzy 't' i 'v' lub t == v oraz warunek na odl +
                    # zawsze ktos sie musi ruszyc + nie moga przebiegac po tej samej krawedzi (3,1) (1,3)

                    if (graph[t][v] or t == v) and v != u and S[u][v] >= k and not (s == u and t == v) and not (s == v and t == u):

                        if not parents[u][v]:
                            parents[u][v] = (s, t)
                            d.append((u, v))

    if parents[y][x] == None: return None

    def get_path(tuple):
        nonlocal x, y
        u, v = tuple[0], tuple[1]
        if u == x and y == v: return [(x, y)]
        return [(u, v)] + get_path(parents[u][v])

    path = [(y, x)] + get_path(parents[y][x])
    return path[::-1]

# runtests(keep_distance)


M=[
[0, 5, 1, 0, 0, 0],
[5, 0, 0, 5, 0, 0],
[1, 0, 0, 1, 0, 0],
[0, 5, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 0]
]

x = 0
y = 5
d = 4

keep_distance(M,x, y, d)