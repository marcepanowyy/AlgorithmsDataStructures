# Heap Sort, kopiec max

def heapify(A, n, i):

    l = 2 * i + 1
    r = 2 * i + 2
    m = i

    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def parent(i):
    return (i-1)//2

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):  # wedrujemy od dolu do gory
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):       # max element na gorze, czyli A[0], jak go wyrzucimy na sam dol i naprawimy kopiec
        A[0], A[i] = A[i], A[0]       # zakladajac ze jest o 1 mniej elementow, to dostaniemy znowu drugi max elem na gorze, potem
        heapify(A, i, 0)              # spychamy go na drugie od konca miejsce i tak dalej

T = [4, 8, 12, 7, 4, 13, 5]

# print(T)
# build_heap(T)
# print(T)



# heap_sort(T)
# print(T)

# import random
# A = [random.randint(0, 99999999) for i in range(10**5)]
# heap_sort(A)
# print(A)

