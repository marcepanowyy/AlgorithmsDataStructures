# Dane jest pelne drzewo binarne T zawierajace n wierzcholkow. Kazdy wezel drzewa zawiera klucz
# bedacy lliczba calkowita. Wezly drzewa numerujmy kolejnymi liczbami naturalnymi w ten sposob
# ze korzen ma nr 1, jego synowie maja numery 2 i 3, nastepny poziom od lewej do prawej, ma
# numery 4,5,6,7, itd. Dany jest ciag X zawierajacy m liczb naturalnych ze zbioru {1,...,n}.
# Nalezy zalozyc, ze m jest istotnie mniejsze niz n. Prosze zaimplementowac funkcje:

# def maxim(T, X):

# ktora zwraca maksymalny klucz sposrod wezlow drzewa T o numerach wymienionych w X.

# Funkcja powinna byc mozliwie jak najsyzbsza - wychodzac z zalozenia ze m << n, i powinna
# dzialac na stalej pamieci (poza pamiecia potrzebna na przechowywanie danych wejsciowych).
# Prosze oszacowac zlozonosc czasowa algorytmu.

# Reprezentacja drzewa. Drzewo reprezentowane jest przy pomocy wezlow typu Node:


class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.parent = None
        self.key = key

# Przyklad. Rozwazmy drzewo, w ktorym klucze warstwami drzewa sa umieszczone tak:

#               5
#            2     3
#          1  0  8   15

# Niech X = [3, 6, 4]. lecture takim razie funkcja maxim powinna zwrocic wartosc 8.

from zad3testy import runtests
from math import floor, log

def get_value(node, i):

    if i == 1: return node.key

    height = 2 ** (int(floor(log(i, 2))) - 1)
    new_i = height + (i % height)

    if i < 3 * height: return get_value(node.left, new_i)

    return get_value(node.right, new_i)


def maxim(T, X):

    max_key = float("-inf")

    for idx in X:
        max_key = max(max_key, get_value(T, idx))

    return max_key

# runtests(maxim)
