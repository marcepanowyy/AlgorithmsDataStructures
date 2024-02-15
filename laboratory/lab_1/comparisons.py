# Funkcja znajdujaca minimum i maksimum w tablicy o
# dl. n, wykonujaca 3/2n + C porownan

def min_max(T):
    l = len(T)
    minimal = float('inf')
    maximal = float('-inf')
    for i in range(0, l-1, 2):
        if T[i] < T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
        if T[i] > maximal:
            maximal = T[i]
        if T[i+1] < minimal:
            minimal = T[i+1]
    return maximal, minimal