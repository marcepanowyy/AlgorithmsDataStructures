# Implementacja wyszukiwania binarnego w posortowanej
# tablicy, znajdujace najmniejszy indeks z dana wartoscia

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