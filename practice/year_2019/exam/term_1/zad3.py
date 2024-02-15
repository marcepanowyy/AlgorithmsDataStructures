# [2pkt.] Zadanie 3.

# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała wieksza od 1 (a>1) zas
# x to liczby rzeczywiste rozlozone rownomiernie na przedziale [0,1]. Napisz funkcje fast_sort, ktora przujmuje tablice
# liczb z wynikami eksperymentu oraz stala a i zwraca tablice z wynikami eksperymentu posortowanymi rosnaco. Funkcja powinna
# dzialac mozliwie jak najszybciej. Uzasadnij poprawnosc zaproponowanego rowziazania i oszacuj zlonosc oblizeniowa
# Naglowek funkcji poiwnien miec postac: def fast_sort(tab, a):

from math import log

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def bucket_sort(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    interval = k / n
    for elem in arr:
        buckets[int(elem // interval)].append(elem)
    i = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for elem in bucket:
            arr[i] = elem
            i += 1

def fast_sort(tab,a):
    n = len(tab)
    res = [0 for _ in range(n)]
    for i in range(n):
        res[i] = log(tab[i], a)
    bucket_sort(res, 1)
    for i in range(n):
        res[i] = a**res[i]
    return res

import copy

T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]

TESTS = [(D1,2), (D2,2), (D3,3)]



def T2S( T ):
    return " ".join([ "%.3f" % x for x in T ] )


def runtests( f ):
    OK = True
    for (T,a) in TESTS:
        BAD = False
        T1 = copy.deepcopy( T )
        T2 = copy.deepcopy( T )
        T.sort()
        print( "tablica            :", T2S(T2) )
        print( "posortowana tablica:", T2S(T) )
        res = f(T1,a)
        print( "wynik programu     :", T2S(res) )

        if len(res) != len(T):
            OK = False
            print("Tablice sa roznych dlugosci")
            continue

        for i in range(len(T)):
            if abs(T[i] - res[i]) > 0.001:
                   BAD = True
                   break
        if BAD:
            OK = False
            print("Blad!")

        print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )

runtests(fast_sort)
