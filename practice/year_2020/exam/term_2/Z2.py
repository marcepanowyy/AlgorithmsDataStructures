# Dane jest drzewo T zawierajace n wierzcholkow. Kazda krawedz e drezwa ma wage w(e) oraz unikalny identyfikator id(e). Waga drezwa jest suma wag jego krawedzi.
# Prosze napisac funkcje

# def balance(T):

# ktora zwraca identyfikator takiej krawedzi e drezwa, ze usuniecie e dzieli drezwo na takie dwa, ktorych roznica wag jest minimalna. Prosze oszacowac zlozonosc czasowa i pamieciowa
# uzytego algorytmu

# Reprezentacja drezwa. Drezwo reprezentowane jest pryz pomocy wezlow typu Node:

class Node:
    def __init__(self):    # stworz wezel drzewa
        self.edges = []    # lista wezlow do ktorych sa krawedzie
        self.weigths = []  # lista wag krawedzi
        self.ids = []      # lista identyfikatorow krawedzi


    def addEdge(self, x, w , id):  # dodaj krawedz  z tego wezla do wezla x,
        self.edges.append(x)       # o wadze w i identyfikatorze id
        self.weigths.append(w)
        self.ids.append(id)

# Pole edges zawiera liste obiektow typu Node. Pola edges, weights oraz ids to listy rownej dlugosci. Nalezy zalozyc, ze drezwo ma co najmniej jedna krawedz.
# Dopuszczalne jest dopisywanie wlasnych pol do Node

# Przyklad

A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6, 1)
A.addEdge(C, 10, 2)
B.addEdge(D, 5, 3)
B.addEdge(E, 4, 4)

# wywoalnie balance(A) powinno zwrocic liczbe 1, czyli identyfikator krawedzi z wezla A do B o wadze 6. Usuniecie jej dzieli nasze drezwo na dwie czesci, o wagach 10
# (krawedz z A do C) oraz 9 (drezwo z korzeniem B i krawedziami do D i E o wagach 4 i 5)

# Dominik Jedraszek
# 1.Dla kazdego wierzcholka x w drzewie T obliczam wage poddrzewa zakorzenionego w x, zapisujac w polu x.sum (funkcja sumTree)
# 2.Idac od korzenia T w dol (po najciezszym dziecku) licze dana roznice bazujac na krawedziach wierzcholka (najmniejsza zapisuje do minRes wraz z ID minId)
# Zlozonosc czasowa: n+h = O(n)
# Zlozonosc pamieciowa: 1(+self.sum)


class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.sum = 0  # suma poddrzewa zakorzenionym w self

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)


def balance(T):

    def sumTree(A):
        a = sum(A.weights)

        for i in A.edges:
            a += sumTree(i)
        A.sum = a

        return A.sum

    def check(A, upSum):
        maxSum = 0
        maxIs = []
        for i in range(len(A.edges)):
            a = abs(upSum + A.sum - A.weights[i] - 2 * A.edges[i].sum)
            nonlocal minRes, minId
            if minRes > a:
                minRes = a
                minId = A.ids[i]

            if maxSum < A.edges[i].sum:
                maxSum = A.edges[i].sum
                maxIs = [i]
            elif maxSum == A.edges[i].sum:
                maxIs.append(i)

        for i in maxIs:
            check(A.edges[i], upSum + A.sum - A.edges[i].sum)

    sumTree(T)

    minRes = inf
    minId = 0
    check(T, 0)

    return minId


# runtests(balance)

"""
    Paweł Zaręba

    Algorytm wykonuje 2 razy przejście algorytmem DFS po całym drzewie

    Za pierwszym razem oblicza dla kazdego węzła sumę drzewa w nim zakorzenionego
    Za drugim razem przegląda kadą krawędź wychodzącą z węzła v i dla niej liczy
    róznicę wag drzew, które powstałyby po jej usunięciu
        Taka róznica wyraza się wzorem abs(w1 - w2), gdzie w1 to waga drzewa na "dolnym"
        końcu krawędzi, a w2 to waga całego drzewa bez wagi rozwazanej krawędzi oraz drzewa,
        którego wagę mamy w w1.

    Poniewaz rozwazany graf jest drzewem to E = O(V), więc oba przejścia DFSem dadzą w sumie
    złozoność obliczeniową O(n)

    Złozoność pamięciowa wynosi O(n) -> pole w kazdym węźle plus pesymistyczna głębokość rekurencji


"""

from math import inf


def balance(T):

    def visit(v):
        v.treeWeight = 0
        for u, w in zip(v.edges, v.weights):
            v.treeWeight += w
            v.treeWeight += visit(u)
        return v.treeWeight

    def visit2(v):
        nonlocal res, resDiff, totalWeight

        for u, w, ind in zip(v.edges, v.weights, v.ids):

            weight1 = u.treeWeight
            weight2 = totalWeight - w - weight1

            if abs(weight1 - weight2) < resDiff:
                resDiff = abs(weight1 - weight2)
                res = ind
            visit2(u)

    res = None
    resDiff = inf
    visit(T)
    totalWeight = T.treeWeight
    visit2(T)

    return res


# runtests(balance)

class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)

    def __str__(self):
        s = "["
        for i in range(len(self.edges)):
            s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
            s += ","
        s += "]"
        return s


def list2tree(L):
    X = Node()
    for CH in L:
        Y = list2tree(CH[2])
        X.addEdge(Y, CH[1], CH[0])

    return X


A = list2tree( [[1,156,[]],[2,829,[]],[5,420,[[4,370,[[3,287,[]],]],]],[6,376,[]],] )
print(balance(A))