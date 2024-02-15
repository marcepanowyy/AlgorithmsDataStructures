# [2pkt.] Zadanie 2.
# Szablon rozwiązania: zad2.py
# Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:

# class Node:
# def __init__(self):
# self.val = None # przechowywana liczba rzeczywista
# self.next = None # odsyłacz do nastepnego elementu

# Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (
# lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy
# znalazłby się na pozycji różniącej się od bieżącej o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem
# 1-chaotycznej listy jest
# 1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
# Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
# Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
# listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
# k = Θ(n).

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):                   # kopiec minimum

    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l][1] < A[m][1]: m = l
    if r < n and A[r][1] < A[m][1]: m = r
    if i != m:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def buildheap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)

class Node:
    def __init__(self):
        self.val = None
        self.next = None

# O(n*log(k))

def SortH(p, k):
    head = Node()
    temp = head
    heap = [None for _ in range(k + 1)]
    node = p
    for i in range(k + 1):
        heap[i] = (node, node.val)
        node = node.next
    buildheap(heap)
    while heap[0][1] != float("inf"):                           # tworzymy kopiec min w ktorym wystepuje k+1 elementow
        temp.next = heap[0][0]                                  # przesuwamy sie wskaznikiem jak posortujemy k+1 elementow
        temp = temp.next                                        # bierzemy najmniejszy i dopinamy do listy
        if node is not None:
            heap[0] = (node, node.val)
            node = node.next
        else:
            heap[0] = (None, float("inf"))
        heapify(heap, len(heap), 0)

    temp.next = None
    return head.next