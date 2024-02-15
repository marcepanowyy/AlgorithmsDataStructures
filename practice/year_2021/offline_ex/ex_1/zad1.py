# takie jak zad.1 na kolosie I 2020/2021

# Paweł Konop

# Algorytm tworzy k+1 elementowy kopiec minimum. Przesuwając się po liscie, brany jest najmniejszy element z kopca
# i jest on dopinany do nowej listy, nastepnie do kopca dodawany jest nowy element z wyjsciowej listy w miejsce
# 'bylego' minimum, naprawiajac za kazdym razem kopiec. Elementami kopca są struktury (node, node.val)
# zlozonosc: nlog(k+1)

# dla k = Θ(1): nlog2
# dla k = Θ(log n): nlog(logn)
# dla k = Θ(n): nlogn

from zad1testy import Node, runtests

def left(i):
    return (2 * i) + 1

def right(i):
    return (2 * i) + 2

def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):

    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] is not None and A[l][1] < A[m][1]:
        m = l
    if r < n and A[r] is not None and A[r][1] < A[m][1]:
        m = r

    if i != m:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def buildheap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)

def SortH(p, k):

    head = Node()
    tail = head

    node = p
    c = 0

    heap = [None for _ in range(k+1)]

    while c < k+1 and node:
        heap[c] = (node, node.val)
        c += 1
        node = node.next

    buildheap(heap)

    while heap[0][1] != float("inf"):
        tail.next = heap[0][0]
        tail = tail.next
        if node is not None:
            heap[0] = (node, node.val)
            node = node.next
        else:
            heap[0] = (None, float("inf"))
        heapify(heap, len(heap), 0)

    tail.next = None
    return head.next

runtests(SortH)


