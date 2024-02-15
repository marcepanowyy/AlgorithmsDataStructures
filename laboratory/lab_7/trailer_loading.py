# Ladowanie przyczepy

# Mamy przyczepe o pojemnosci K kilogramow oraz zbior ladunkow
# o wagach w1, ..., wn. Waga kazdego z ladunkow jest potega dwojki
# (czyli na przyklad, dla siedmiu ladunkow wagi moga wynosic 2, 2, 4, 8, 1, 8, 16,
# a pojemnosc przyczepy K = 27).

# Prosze podac algorytm zachlanny i uzasadnic jego
# poprawnosc, ktory wybiera ladunki tak, ze przyczepa jest mozliwie maksymalnie
# zapelniona, ale bez przekraczania pojemnosci i jednoczesnie uzylismy mozliwie
# jak najmniej ladunkow.

#(Ale jesli da sie np. zaladowac przyczepe do pelna
# uzywajac 100 ladunkow, albo zaladowac do pojemnosci K-1 uzywajac jednego ladunku,
# to lepsze jest to pierwsze rozwiazanie)

def trailer_loading(T, k):
    n = len(T)
    T.sort(reverse=True)
    res = []
    for w in T:
        if k - w >= 0:
            res.append(w)
            k -= w
    return res

T = [2, 2, 4, 8, 1, 8, 16]
K = 27

# print(trailer_loading(T, K))


