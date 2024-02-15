# [2pkt.] Zadanie 1.
# Szablon rozwiązania: zad1.py
# Drzewo przedziałowe: inttree.py

# Dana jest lista I przedziałów domkniętych [a1, b1], [a2, b2], . . . ,[an, bn]. Napisz funkcję intervals(
# I ), która oblicza dla każdego i ∈ {1, 2, . . . , n} długość najdłuższego ciągłego przedziału, który
# można osiągnąć sumując wybrane przedziały spośród pierwszych i przedziałów z listy. Funkcja
# powinna być możliwie jak najszybsza.
# Przedziały reprezentowane są w postaci listy par. Funkcja powinna zwrócić listę liczb, w której i-ty
# element to długość poszukiwanego najdłuższego przedziału zbudowanego z pierwszych i elementów
# wejścia.

# Na przykład, dla listy odcinków:

# [(1,3),(5,6),(4,7),(6,9)]

# rozwiązaniem jest lista [2, 2, 3, 5] zawierająca długości odcinków: [1, 3], [1, 3], [4, 7]
# oraz [4, 9].
# Drzewo przedziałowe

# lecture pliku inttree.py została Państwu dostarczona elementarna implementacja drzewa przedziałowego, tak jak było ono opisane na wykładzie. Dostępne są następujące funkcje:

# 1. tree(A) – stwórz nowe drzewo przedziałowe; przechowywane przedziały muszą być postaci
# [a, b], gdzie liczby a i b występują w tablicy A; tablica A musi być posortowana rosnąco i nie
# może zawierać powtórzeń. Funkcja zwraca korzeń drzewa T. Złożoność: O(∣A∣).

# 2. tree insert(T, (a,b)) – wstaw do drzewa T (reprezentowanego przez korzeń) przedział
# [a, b]. Złożoność: O(log ∣A∣).

# 3. tree remove(T, (a,b)) – usuń z drzewa T (reprezentowanego przez korzeń) przedział [a, b]
# (jeśli przedziału nie było w drzewie, to nic nie robi). Złożoność: O(log ∣A∣).

# 4. tree intersect( T, x ) – zwraca listę przedziałów z drzewa T (reprezentowanego przez
# korzeń), które zawierają punkt x (niektóre przedziały mogą występować na liście dwukrotnie).
# Złożoność: O(k + log ∣A∣), gdzie k to liczba zwróconych przedziałów

# 5. tree print( T ) – funkcja pomocnicza wypisująca zawartość drzewa (proszę zajrzeć do kodu,
# żeby zobaczyć co wypisuje).

# Nie ma obowiązku korzystać z tego drzewa—można zaimplementować własne, lub użyć innej
# struktury danych. Jeśli ktoś zaimplementuje klasyczne drzewo bst to może je analizować tak,
# jakby operacje na nim miały złożoność O(log n)}.

# implementacja drzewa przedzialowego -- wolno uzyc na kolokwium 3
# Algorytmy i Struktury Danych 2020
#
# Zlozonosci przy algorytmach sa takimi, jakie nalezy zalozyc przy
# analizie wlasnego kodu (faktyczna implementacja jest w niektorych przypadkach troche
# wolniejsza)

class Node:
    def __init__(self):
        self.cut = None  # klucz tego wezla
        self.left = None  # span = [self.left, self.right]
        self.right = None
        self.intervals = []  # przedzialy zgromadzone w tym wezle
        self.lchild = None  # lewe dziecko
        self.rchild = None  # prawe dziecko
        self.leaf = False  # czy to lisc?


# funkcja pomocnicza do budowania drzewa
def tree_build(A, i, j, left, right):
    X = Node()
    X.left = left
    X.right = right
    if (j < i):
        # build leaf
        X.cut = -1
        X.leaf = True
    else:
        # build internal node
        m = (i + j) // 2
        X.cut = A[m]
        X.lchild = tree_build(A, i, m - 1, left, A[m])
        X.rchild = tree_build(A, m + 1, j, A[m], right)
    return X


# zbuduj drzewo przedzialowe, ktore moze przechowywac
# przedzialy postaci [a,b], gdzie a,b to punkty z tablicy A
# tablica A musi byc posortowana rosnaco i bez powtorzen
#
# Zlozonosc: O(n), gdzie n to rozmiar A
def tree(A):
    return tree_build(A, 0, len(A) - 1, min(A) - 1, max(A) + 1)


# Wypisz zawartosc drzewa X
def tree_print(X, ind=""):
    if X.leaf:
        print(ind, "leaf-span: [%d, %d] --> " % (X.left, X.right), X.intervals);
    if not X.leaf:
        print(ind, "cut = %d," % X.cut, "span = [%d, %d], " % (X.left, X.right), "intervals =", X.intervals);
        tree_print(X.lchild, ind + "  ")
        tree_print(X.rchild, ind + "  ")


# funkcja pomocnicza wykonujaca operacje na zadanym przedziale
def tree_op(X, I, f):
    (a, b) = I
    if a <= X.left and b >= X.right:
        f(X, I)
        return
    if a < X.cut:
        tree_op(X.lchild, I, f)
    if b > X.cut:
        tree_op(X.rchild, I, f)


# funkcja pomocnicza
def op_insert(X, I):
    X.intervals.append(I)


# funkcja pomocnicza
def op_remove(X, I):
    try:
        X.intervals.remove(I)
    except ValueError:
        None


# Wstawia przedzial I do drzewa X
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_insert(X, I):
    tree_op(X, I, op_insert)


# Usuwa przedzial I z drzewa X (jesli przedzialu nie ma, to nic nie robi)
# Zlozonosc: O(log n), gdzie n to liczba punktow na bazie ktorych powstalo drzewo
def tree_remove(X, I):
    tree_op(X, I, op_remove)


# zwraca liste wszystkich przedzialow z drzewa X, ktore zawieraja punkt a
# UWAGA: niektore przedzialy moga wystepowac dwa razy
#
# Dziala w czasie O(logn + k), gdzie n to liczba punktow na bazie
# ktorych powstalo drzewo a k to liczba znalezionych przedzialow
def tree_intersect(X, a):
    R = X.intervals.copy()
    if X.leaf:
        return R
    if a <= X.cut:
        R += tree_intersect(X.lchild, a)
    if a >= X.cut:
        R += tree_intersect(X.rchild, a)
    return R


def run_tests(intervals):
    A = [(1, 3), (5, 6), (4, 7), (6, 9), (3, 5)]
    A_res = [2, 2, 3, 5, 8]
    B = [(7, 9), (0, 7), (10, 20), (7, 10)]
    B_res = [2, 9, 10, 20]
    C = [(1, 2), (5, 8), (9, 13), (14, 16), (2, 6), (13, 15), (3, 4), (11, 12), (7, 10)]
    C_res = [1, 3, 4, 4, 7, 7, 7, 7, 15]

    t = 0
    error = False
    for (X, X_res) in [(A, A_res), (B, B_res), (C, C_res)]:
        t += 1
        print("Test", t)
        print("Dane:", X)
        print("Oczekiwany wynik:", X_res)
        S_res = intervals(X)
        print("Uzyskany wynik  :", S_res)

        if len(S_res) != len(X_res):
            print("Zly rozmiar listy")
            error = True
        else:
            for i in range(len(X_res)):
                if S_res[i] != X_res[i]:
                    print("Blad w tescie")
                    error = True
                    break
        print("-------------")

    if error:
        print("Bledy!")
    else:
        print("OK!")
    exit(0)

# Przykład wykorzystania drzewa przedziałowego
# T = tree([1, 2, 3, 4, 5])
# tree_insert(T,(1, 4))
# tree_insert(T,(2, 5))
# tree_print(T)
# tree_remove(T,(1, 4))
# tree_print(T)
# tree_insert(T,(1, 3))
# print(tree_intersect(T, 3))