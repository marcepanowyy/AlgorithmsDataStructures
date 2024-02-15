# Dana jest lista L parami roznych napisow skladajacych sie z symobli 0, 1. Mowimy ze pewien napis s
# jest fajny, jesli jest prefiksem co najmniej dwoch napisow z L (przy czym jesli w L znajduje sie
# napis identyczny z s, to napis s wciaz traktujemy jako jego prefiks). Dalej, mowimy, ze napis s
# jest bardzo fajny, jesli jest fajny a zarazem zadne jego rozszerzenie (poprzez dodanie dowolnego
# symbolu na koncu) nie jest napisem fajnym.

# Zaproponuj, uzasadnij poprawnosc i zaimplementuj algorytm, ktory otrzymuje liste napiow L
# (skladajacych sie z zer i jedynek) i zwraca wszystkie bardzo fajne napisy dla tej listy. Algorytm
# powininen byc zaimplementowany jako funkcja postaci:

# def double_prefix(L):
#   ...

# gdzie L to lista zawierajace wejsciowe napisy (jako napisy w jezyku Python). Funkcja powinna
# zwrocic liste prefiksow spelniajacych warunki zadania (rowniez jako liste napisow jezyka Python).
# Prefiksy mozna zwrocic w dowolnej kolejnosci.

# Przyklad. Dla wejscia ['0100', '0110', '1010', '1'] prawidlowym wynikiem jest dowolna permutacja
# listy ['01', '1']

from zad2testy import runtests

# wzorcowka O(D) (D - sumaryczna dlugosc wszystkich sekwencji)
# tworzymy drzewo prefiksowe

class Node:
    def __init__(self, char):
        self.right = None
        self.left = None
        self.parent = None
        self.char = char
        self.c = 0

def create_tree(L):

    def insert_string(tree, string):
        for c in string:
            if c == '0':
                if tree.left:
                    tree = tree.left
                else:
                    new_node = Node('0')
                    tree.left = new_node
                    new_node.parent = tree
                    tree = tree.left

            else:
                if tree.right:
                    tree = tree.right
                else:
                    new_node = Node('1')
                    tree.right = new_node
                    new_node.parent = tree
                    tree = tree.right

            tree.c += 1

    tree = Node('-1')

    for string in L:
        insert_string(tree, string)

    return tree

def get_leaves(tree):

    leaves = []

    def dfs(tree):

        is_leaf = True

        if tree.left and tree.left.c >= 2:
            is_leaf = False
            dfs(tree.left)
        if tree.right and tree.right.c >= 2:
            is_leaf = False
            dfs(tree.right)
        if is_leaf:
            leaves.append(tree)

    if tree.left: dfs(tree.left)
    if tree.right: dfs(tree.right)

    return leaves


def get_str(leaf):

    if leaf.char == '-1': return ''
    return leaf.char + get_str(leaf.parent)

def double_prefix(L):

    tree = create_tree(L)
    leaves = get_leaves(tree)
    res = []

    for leaf in leaves:
        res.append(get_str(leaf)[::-1])

    return res

# runtests(double_prefix)

