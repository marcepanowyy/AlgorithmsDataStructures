# [2pkt.] Zadanie 1.
# Szablon rozwiązania: zad1.py
# lecture tym zadaniu nie wolno korzystać z wbudowanych funkcji sortowania!
#
# Mówimy, że tablica T ma współczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli speł-
# nione są łącznie dwa warunki:
#
# 1. tablicę można posortować niemalejąco przenosząc każdy element A[i] o co najwyżej k pozycji
# (po posortowaniu znajduje się on na pozycji różniącej się od i co najwyżej o k),
# 2. tablicy nie da się posortować niemalejąco przenosząc każdy element o mniej niż k pozycji.
#
# Proszę zaproponować i zaimplementować algorytm, który otrzymuje na wejściu tablicę liczb rze-
# czywistych T i zwraca jej współczynnik nieuporządkowania. Algorytm powinien być jak najszybszy
#
# oraz używać jak najmniej pamięci. Proszę uzasadnić jego poprawność i oszacować złożoność obli-
# czeniową. Algorytm należy zaimplementować jako funkcję:
#
# def chaos_index( T ):
# ...
#
# przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieupo-
# rządkowania.
#
# Przykład. Dla tablicy:
# T = [0, 2, 1.1, 2]
# prawidłowym wynikiem jest k = 1.

# ROZWIAZANIE ASI:

# w algorytmie korzystam ze zmodyfikowanego algorytmu sortowania Mergesort, który sortuje dane po pierwszej współrzędnej
# (Mergesort, bo jest to sortowanie stabilne). Tworzę dodatkową tablicę która zawiera podtablice postaci [liczba w tablicy
# wejściowej, jej indeks w tablicy wejściowej]. Sortuje tę tablicę po 1 współrzędnej i sprawdzam jaka jest różnica między
# położeniem w wejściowej tablicy a tej dodatkowej tablicy i nadpisuje tą różnicą wartość w dodatkowej tablicy. Następnie wyznaczam
# maksimum czyli maksymalną różnicę w położeniu danej liczby w obu tablicach. Jest to szukane k.
# Złożoność algorytmu to O(nlogn) (czyli tyle co Mergesort), algorytm zużywa dodatkowo n pamięci ("dodatkowa" tablica).

def merge_sort(t, tmp, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(t, tmp, l, mid)
        merge_sort(t, tmp, mid + 1, r)
        i = k = l
        j = mid + 1
        while i <= mid and j <= r:
            if t[i][0] <= t[j][0]:
                tmp[k] = t[i]
                i += 1
            else:
                tmp[k] = t[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = t[i]
            i += 1
            k += 1
        while j <= r:
            tmp[k] = t[j]
            j += 1
            k += 1
        for q in range(l, r + 1):
            t[q] = tmp[q]
    return t

def mergesort(t):
    n = len(t)
    tmp = [[0,0] for _ in range(n)]
    return merge_sort(t, tmp, 0, n - 1)

def chaos_index(T):
    n = len(T)
    res = []
    for i in range(n):
        res.append([T[i], i])
    mergesort(res)
    for i in range(n):
        res[i] = abs(res[i][1] - i)
    return max(res)
