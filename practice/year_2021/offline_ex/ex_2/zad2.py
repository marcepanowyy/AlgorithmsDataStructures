# takie jak zad.6 z zestawu nr II z cwiczen

# Paweł Konop
# aby znalezc maksimum szukanego przedzialu musimy posortowac tablice wzgledem pierwszego indeksu, potem drugiego indeksu
# (dodajac po kazdym sortowaniu indeksy, ktore odpowiadaja kolejnosci wystapien), nastpenie porownujemy indeksy ktore stoja
# na pozycji 2 i 3 (liczac od zera), aby znalezc interesujacy nas przedzial. Potem szukamy maksimum, iterujac po przedzialach,
# sprawdzajac czy przedzial [a,b] zawiera sie calkowicie w znalezionym przedziale.

from zad2testy import runtests

from random import randint

def partition(T, p, r, index):
    random_index = randint(p, r)
    # random_index = 0
    T[random_index], T[r] = T[r], T[random_index]
    pivot = T[r][index]
    i = p - 1
    for j in range(p, r):
        if T[j][index] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1

def quicksort(T, p, r, index):
    while p < r:
        q = partition(T, p, r, index)
        if q - p <= r - q:
            quicksort(T, p, q - 1, index)
            p = q + 1
        else:
            quicksort(T, q, r, index)
            r = q - 1

def depth(T):
    quicksort(T, 0, len(T) - 1, 0)
    for i in range(len(T)):
        T[i] = (T[i][0], T[i][1], i)
    quicksort(T, 0, len(T) - 1, 1)
    for i in range(len(T)):
        T[i] = (T[i][0], T[i][1], T[i][2], i)
    max_interval = max_index = 0
    for i in range(len(T)):
        if T[i][3] - T[i][2] > max_interval:
            max_interval = T[i][3] - T[i][2]
            max_index = i
    c = -1
    for i in range(len(T)):
        if (T[i][0] >= T[max_index][0] and T[i][1] <= T[max_index][1]):
            c += 1
    return c

runtests(depth)


