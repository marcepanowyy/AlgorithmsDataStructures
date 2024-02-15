# Quick Select

# znajduje wartosc pod wskazanym indeksem po posortowaniu tablicy

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def select(A, p, r, k):   # przewaznie dziala w czasie liniowym
    if p == r: return A[p]
    q = partition(A, p, r)
    if q == k: return A[q]
    elif k < q: return select(A, p, q-1, k)
    else: return select(A, q+1, r, k)

T = [12, 4, 5, 24, 100, 99, 42, 41, 2, -1, 42, 5]

print(select(T,0,len(T)-1,4))
# print(select(T,0,len(T)-1,len(T)-1))
print(T)


# T = [9, 5, 3, 8, 0, 4, 1, 7, 2, 6]
# x = select(T, 5, len(T)-1, 9)
# print(x)
# print(T)

