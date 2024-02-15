# [2pkt.] Zadanie 1.

# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
# są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
# aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
# podać złożoność czasową i pamięciową zaproponowanego algorytmu.

# Przykład. Dla tablicy:
# T = [ [ 2, 3, 5],
#       [ 7,11,13],
#       [17,19,23] ]
# wynikiem jest, między innymi tablica:
# T = [ [13,19,23],
#     [ 3, 7,17],
#     [ 5, 2,11] ]

# Algorytm na początku znajduje największy i najmniejszy element (za pomocą zmodyfikowanego algorytmu quickselect)
# ze zbioru elementów o długości n, który znajdowałby się
# na środku tablicy T gdyby była ona posortowana i liniowa (te elementy miałyby indeksy (n**2-n)/2 oraz (n**2+1)/2+1).
# Po takie operacji tablicę T mozna podzielic na 3 podtablice - 1)elementy mniejsze od tych, które będą na przekątnej,
# 2) elementy które będą na przekątnej, 3)elementy większe od tych na przekątnej.
# Następnie algorytm umieszcza właściwe elementy na przekątnej głównej, zamieniając je z elementami w taki sposób, ze
# elementy mniejsze od nich lądują nad przekątną, a mniejsze pod nią.
# Na końcu algorytm zamienia elementy większe od tych na przekątnej, które znajdują się pod nią, z elementami mniejszymi nad nią.
#
# Złozoność obliczeniowa: O(n2)
# Złozoność pamięciowa: O(n2) (nie jest uzywana zadna pamiec ponad ta ktora zajmuje tablica T)


def partition(tab, left, right):
    n = len(tab)
    piv = tab[right // n][right % n]
    i = left - 1
    for j in range(left, right):
        if tab[j // n][j % n] < piv:
            i += 1
            tab[j // n][j % n], tab[i // n][i % n] = tab[i // n][i % n], tab[j // n][j % n]
    i += 1
    tab[right // n][right % n], tab[i // n][i % n] = tab[i // n][i % n], tab[right // n][right % n]
    return i


def quickselect(tab, left, right, k):
    if k > 0 and k <= right - left + 1:
        piv = partition(tab, left, right)

        if piv - left == k - 1:
            n = len(tab)
            return tab[piv // n][piv % n]

        if piv - left > k - 1:
            return quickselect(tab, left, piv - 1, k)
        return quickselect(tab, piv + 1, right, k - piv + left - 1)

    return float("inf")


def Median(T):
    n = len(T)
    min_med = quickselect(T, 0, n ** 2 - 1, (n ** 2 - n) / 2 + 1)
    max_med = quickselect(T, 0, n ** 2 - 1, (n ** 2 + n) / 2)
    diag_ind = 0
    ind = (n ** 2 - n) // 2
    for i in range(1, n + 1):  # umieszczanie właściwych elementów na przekątnej
        T[ind // n][ind % n], T[diag_ind // n][diag_ind % n] = T[diag_ind // n][diag_ind % n], T[ind // n][ind % n]
        ind += 1
        diag_ind = n * i + i

    row_len = n - 1
    for i in range(n // 2):  # zamiana elementów większych od tych na przekątnej które są pod nią z mniejszymi, które są nad nią
        for j in range(row_len):
            small_ind = n - row_len + j
            big_ind = row_len - 1 - j
            T[i][small_ind], T[n - i - 1][big_ind] = T[n - i - 1][big_ind], T[i][small_ind]
        row_len -= 1

    return

# if __name__ == "__main__":
#     tab = [ [2,3,5], [7,11,13], [17,19,23] ]
#     Median(tab)
#
