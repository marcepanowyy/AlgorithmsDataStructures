# Implementacja wyszukiwania binarnego w posortowanej
# tablicy, znajdujace najmniejszy indeks z dana wartoscia x

def binary_search(T, b, e, x): # begin, end
    if b > e: return None
    c = (b + e) // 2
    if T[c] == x:
        res = binary_search(T, b, c-1, x)
        if res == None: return c
        return res
    if T[c] > x:
        return binary_search(T, b, c-1, x)
    else:
        return binary_search(T, c+1, e, x)

T = [1, 4, 5, 5, 5, 5, 10]
# print(binary_search(T, 0, len(T)-1, 5))

def it_binary_search(T, b, e, x):
    while b <= e:
        c = (b+e)//2
        if T[c] == x:
            p = c
            while T[p] == T[c]:
                c -= 1
            return c+1

        elif T[c] > x: e = c-1
        else: b = c + 1
    return None

T = [1, 4, 5, 5, 5, 5, 10]
# print(it_binary_search(T, 0, len(T)-1, 5))
