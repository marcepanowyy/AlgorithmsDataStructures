# Algorytm tworzy nowa tablice, ktora zawiera pojemnosc magazynu pod i-tym
# indeksem. Nastepnie tworzy drzewo przedzialowe, aby udostepnic wyszukanie
# magazynu o najmniejszym indeksie, ktory pomiesci i-ty transport oraz zmiane
# pojemnosci tego magazynu w czasie O(logn). lecture petli algorytm przechodzi
# po wszystkich transportach i znaduje odpowiedni magazyn. Zwracany jest indeks,
# do ktorego powedrowal ostatni transport.

# Zlozonosc czasowa: O(nlogn)
# Zlozonosc pamieciowa: O(n) 


from egz2atesty import runtests


class ST: # Segment Tree
    def __init__(self, intLeft, intRight) -> None:
        self.left = None
        self.right = None
        self.intLeft = intLeft
        self.intRight = intRight
        self.val = 0
        self.idx = -1


def buildTree(A, l, r):
    if l == r:
        root = ST(l, r)
        root.val = A[l]
        root.idx = l
        return root
    if l < r:
        root = ST(l, r)
        m = l + (r - l) // 2
        root.left = buildTree(A, l, m)
        root.right = buildTree(A, m + 1, r)
        root.val = max(root.left.val, root.right.val)
    return root


def findIdx(root, x):
    if root.left is None and root.right is None:
        return root.idx
    if root.left.val >= x:
        return findIdx(root.left, x)
    return findIdx(root.right, x)


def changeVal(root, idx, val):
    if root.idx == idx:
        root.val -= val
        return val
    m = root.intLeft + (root.intRight - root.intLeft) // 2
    if idx <= m:
        changeVal(root.left, idx, val)
    else:
        changeVal(root.right, idx, val)
    root.val = max(root.left.val, root.right.val)


def coal( A, T ):
    n = len(A)
    capacity = [T for _ in range(n)]
    root = buildTree(capacity, 0, n - 1)
    idx = 0
    for i in range(n):
        idx = findIdx(root, A[i])
        changeVal(root, idx, A[i])
    return idx

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( coal, all_tests = True )
