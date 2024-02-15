# [2pkt.] Zadanie 3.
# Szablon rozwiązania: zad3.py
# Dana jest struktura realizująca listę jednokierunkową:

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

# Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
# w jedną posortowaną listę (składającą się z tych samych elementów).
# Przykład Dla tablicy [[0,1,2,4,5],[0,10,20],[5,15,25]] - po przekształceniu jej elementów
# z Python’owskich list na listy jednokierunkowe - wynikiem powinna być lista jednokierunkowa, która
# po przekształceniu jej na listę Python’owską przyjmie postać [0,0,1,2,4,5,5,10,15,20,25].

def print_List(L):
    if L is not None:
        print(L.val, end=" ")
        print_List(L.next)
    else:
        print()

def tab_to_list(tab):

    n = len(tab)
    if n == 0:
        return None

    L = Node(None)
    head = L

    for i in range(n):
        L.next = Node(tab[i])
        L = L.next

    return head.next

# HeapSort, kopiec min

def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l][1] < A[m][1]: m = l
    if r < n and A[r][1] < A[m][1]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def parent(i):
    return (i-1)//2

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):  # wedrujemy od dolu do gory
        heapify(A, n, i)

def build_heap1(A):
    n = len(A)
    for i in range((n-2)//2, -1, -1):  # wedrujemy od dolu do gory
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):       # max element na gorze, czyli A[0], jak go wyrzucimy na sam dol i naprawimy kopiec
        A[0], A[i] = A[i], A[0]       # zakladajac ze jest o 1 mniej elementow, to dostaniemy znowu drugi max elem na gorze, potem
        heapify(A, i, 0)              # spychamy go na drugie od konca miejsce i tak dalej


def merge(T):   # T - tablica z posortowanymi listami jednokier.

    n = len(T)
    head = Node(None)
    temp = head
    heap = [None for _ in range(n)]                 # tworzymy podstawe kopca
    for i in range(n):                              # wypełniamy go pierwszymi n node'ami oraz wartosciami node'ow
        heap[i] = T[i], T[i].val, i
        T[i] = T[i].next

    build_heap(heap)                                # budujemy kopiec

    while heap[0][1] != float("inf"):
        temp.next, nr = heap[0][0], heap[0][2]
        temp = temp.next
        if T[nr] is not None:
            heap[0] = (T[nr], T[nr].val, nr)        # przechowujemy w heap[0]:    wezel, wartosc wezla, numer indeksu tablicy z ktorej jest ten wezel
            T[nr] = T[nr].next
        else:
            heap[0] = (None, float("inf"), None)
        heapify(heap, n, 0)

    temp.next = None
    return head.next

A = [[0,1,2,4],[0,10,20]]
for i in range(len(A)):
    A[i] = tab_to_list(A[i])


# x = merge(A)
# print_List(x)

# ROZW MATIEGO

""" O(n * log(n)) """

# from zad3testy import runtests

from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def add_sentinels(L):
    n = len(L)
    for i in range(n):
        sentinel = Node(None)
        sentinel.next = L[i]
        L[i] = sentinel

def get_length(head):
    length = 0
    curr = head.next
    while curr:
        length += 1
        curr = curr.next
    return length


def _merge(head1, head2):

    curr1 = head1.next
    curr2 = head2.next
    head = tail = Node(None)

    while curr1 and curr2:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    if curr1:
        tail.next = curr1
    else:
        tail.next = curr2

    return head


def merge_lists(L):
    n = len(L)
    if not L: return None
    if n == 1: return L[0]
    # For each list add a sentinel node
    add_sentinels(L)
    # Get length of each list and add this list with its length
    # as a priority to the minimum priority queue
    pq = PriorityQueue()
    # Second value is a placeholder to allow Python's comparisons
    # when a priority is the same
    i = 0
    while i < n:
        pq.put((get_length(L[i]), i, L[i]))
        i += 1
    # In a loop, merge lists of the lowest length together and add
    # a resulting list back to the priority queue
    while True:
        length1, _, head1 = pq.get()
        length2, _, head2 = pq.get()
        new_head = _merge(head1, head2)
        new_length = length1 + length2
        if not pq.empty():
            pq.put((new_length, i, new_head))
            i += 1
        else:
            return new_head.next

# runtests(merge_lists)