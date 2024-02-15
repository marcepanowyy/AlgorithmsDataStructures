# Drzewo bst T reprezentowane jest przez obiekty klasy Node:

class Node:
    def __init__(self):
        self.left = None        # lewe poddrzewo
        self.right = None       # prawe poddrzewo
        self.parent = None      # rodzic drzewa jeśli istnieje
        self.value = None       # przechowywana wartość

# Proszę zaimplementować funkcję:

# def ConvertTree(T):
#    ...

# która przekształca drzewo T na drzewo o minimalnej wysokości, w którym węzły spełniają warunek:
# największy element na danym poziomie jest mniejszy od najmniejszego elementu na kolejnym poziomie.
# Funkcja zwraca korzeń nowego drzewa. Poziomy numerujemy od korzenia do liści. Funkcja powinna być
# możliwie jak najszybsza oraz - jako kryterium drugiego rzędu - używać jak najmniejszej ilości pamięci
# (poza pamięcią już wykorzystaną na reprezentacje drzewa). Proszę oszacować złożoność czasową oraz
# pamięciową użytego algorytmu.

# Przyklad poprawnego przeksztalcenia.

#                    11                           2
#                   /  \                         / \
#                  3    13                      3   5
#                 / \                          / \   \
#                2   7                       11   7   13
#                   /
#                  5

#################### ROZW ZA 1 pkt

def ConvertTree(tree):

    def put_in_order(tree):

        if tree:
            put_in_order(tree.left)    # dodajemy node'y do listy
            list.append(tree)          # z posortowanymi wartosciami
            put_in_order(tree.right)   # (wykorzystujemy wlasnosc bst)

    list = []

    put_in_order(tree)
    n = len(list)

    for i in range(n):
        list[i].left = list[2*i+1] if 2*i+1 < n else None     # drzewo binarne
        list[i].right = list[2*i+2] if 2*i+2 < n else None
        list[i].parent = list[(i-1)//2] if i > 0 else None

    return list[0]

#########################

from zad1testy import runtests

runtests(ConvertTree)