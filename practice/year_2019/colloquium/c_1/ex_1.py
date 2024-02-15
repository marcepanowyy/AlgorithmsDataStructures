# [2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

# rozwiazanie bitalgostart -> 25 marzec -> z8

# Cyfra jednokrotna to taka, tkora wystepuje w danej liczbie dokladnie 1 raz
# cyfra wielokrotna to taka, ktora w liczbie wystepuje wiecej niz jeden raz

# Mowimy ze liczba naturalna A jest ladniejsza od liczby naturalnej B
# jezeli w liczbie A wystepuje wiecej cyfr jednokrotnych niz  wB
# a jezeli cyfr jednokrotych jest tyle samo, to ladniejsza jest ta liczba
# ktora posiada mniej cyfr wielokrotnych. Na przyklad
# liczba 123 jest ladniejsza od 455. Liczba 1266 jest ladniejsza od 114577
# a liczby 2344 i 67333 sa jednakowo ladne

# dana jest tablica T zawierajaca liczby naturalne. Prosze zaimplementowac
# funkcje: pretty_sort(T), ktora sortuje elementy tablicy T od najladniejszych
# do najmniej ladnych. Uzyty algorytm powinien byc jak najszybszy.


def modify(num):
    D = [0] * 10
    while num != 0:
        D[num%10] += 1
        num //= 10
    single = 0
    multi = 0
    for i in range(10):
        if D[i] == 1:
            single += 1
        if D[i] > 1:
            multi += 1
    return(100*single + multi)

def find_max(T):
    n = len(T)
    max_ = -1
    for i in range(n):
        if T[i][1] > max_: max_ = T[i][1]
    return max_

def radix_sort(arr):
    maximum = find_max(arr)
    div = 1
    while maximum // div != 0:
        counting_sort(arr, div)
        div *= 10
    return arr

def counting_sort(arr, div):
    n = len(arr)
    c_arr = [0] * 10
    output = [0] * n

    for i in range(n):
        index = (arr[i][1] // div) % 10
        c_arr[index] += 1

    for i in range(1, 10):
        c_arr[i] += c_arr[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i][1] // div) % 10
        output[c_arr[index] - 1] = arr[i]
        c_arr[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], modify(T[i]))
    radix_sort(T)
    for i in range(n):
        T[i] = T[i][0]
    return T

# T = [123, 455, 1266, 114577, 2344, 67333]
# print(pretty_sort(T))