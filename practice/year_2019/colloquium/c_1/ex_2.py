# [2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową

#funkcja szuka wzrostu osoby p i q

def element(tab, numer, poczatek, koniec):
    if poczatek == koniec:
        return tab[poczatek]
    val = tab[koniec]
    i = poczatek - 1
    for j in range(poczatek, koniec):
        if tab[j] >= val:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[koniec], tab[i + 1] = tab[i + 1], tab[koniec]
    if i - poczatek + 2 == numer:
        return tab[i + 1]
    if i - poczatek + 2 < numer:
        return element(tab, numer - i + poczatek - 2, i + 2, koniec)
    return element(tab, numer, poczatek, i)


def section(tab, p, q):
    liczba_zolniezy = p - q + 1
    dlugosc = len(tab)
    pierwszy = element(tab, dlugosc - p, 0, dlugosc - 1)
    #da wzorst czloweika p ( szuka katego wzoostu wzgledem wzostu, wiec dlugosc-p)
    ostatni = element(tab, dlugosc - q, 0, dlugosc - 1)
    tablica = [0] * liczba_zolniezy
    tablica[0] = pierwszy
    tablica[liczba_zolniezy - 1] = ostatni
    j = 1
    #znajdue pozostałych ludzi, ktorzy powinni tam być
    for i in range(dlugosc):
        if tab[i] > pierwszy and tab[i] < ostatni:
            tablica[j] = tab[i]
            j = j + 1
    print(tablica)

#zlozonosc funkcji element  uznaje sie za O(n), wywoalnie jej dwa razy to dalej 0(n)
#for tez mam 0(n), co daje zlozonosc liniowa
#nie jest napisane, aby zworocic ta tablice posortowana, wiec tego nie robie
#jesli mialbym to zrobic to zloznosc maksymalnie moze wyniesc O(dlugosc*logdlugosc)
#ale o tym mowy nie było, wiec mamy zlozonosc liniowa

# T = [0.8, 1.8, 1.9, 1.6, 1.65, 1.9]
# for i in range(len(T)):
#     T[i] = T[i] * 100
# section(T, 1, 3)

# ALBO

def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x > q:
        return quick_select(T, q + 1, r, x)
    else:
        return quick_select(T, p, q - 1, x)


T = [8, 1, 2, 7, 3, 5, 6, 4, 0]
x = quick_select(T, 0, 8, 4)
print(x)
print(T)

def sumBetween(T, s, e):
     n = len(T)
     quick_select(T, 0, n - 1, s)
     quick_select(T, 0, n - 1, e)
     print(T)
     counter = 0
     for i in range(s, e + 1):
         counter += T[i]

     return counter

