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