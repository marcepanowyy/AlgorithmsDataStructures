# Cel: dana jest tablica A zawierajaca liczby naturalne
# nie mniejsze od 1. poczatkowo stoimy na pozycji 0.
# wartosc A[i] informuje nas jaka jest maksymalna dlugosc
# skoku na nastepna pozycje

# przyklad A = [1,3,2,1,0]

# z pozycji 0 moge przejsc na pozycje 1. z pozycji 1 moge
# przejsc na 2,3,4. Nalezy podac na ile sposobow moge przejsc
# z pozycji 0 na pozycje n-1, przestrzegajac regul tablicy

def amazon_stairs(A):

    n = len(A)
    T = [0] * n
    T[0] = 1

    for i in range(1, n):
        num = A[i]
        k = i+1
        T[i] += T[i-1]
        while num != 0 and k < n:
            T[k] += 1
            k += 1
            num -= 1

    return T[n-1]

A = [1, 3, 2, 1, 0]
B = [2, 1, 3, 2, 2, 3]
# print(amazon_stairs(B))