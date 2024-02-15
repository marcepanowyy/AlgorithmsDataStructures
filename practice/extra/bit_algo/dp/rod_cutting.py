# Firma kupuje dlugie stalowe prety i tnie je na kawalki, ktore sprzedaje.
# kawalki maja dlugosc w metrach wyrazona zawsze liczba naturalna.
# Dla kawalka dlugosci n metrow znane sa ceny kawalko dlugosci
# 1, 2, ..., n metrow. Firma chce znac maksymalny zysk, ktory moze uzyskac
# z pociecia i sprzedania preta dlugosci n

# np dla T = [0,2,3,7,8,4,2,4,2,1]
# i preta dlugosci 10

# Tworzymy tablice, ktora informuje nas
# ile max zarobimy za dlugosc preta (index)
# np:
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 2 ... itp (maksymalny zysk za pret dl. 1 to 2) szukamy teraz maksymalnego zysku
# dla preta dlugosci 2 itp...

# f(i) = max(f(i-k) + T[k]) k = {0, 1, ... i}

# O(n**2)

def rod_cutting(T):
    n = len(T)
    profit = [0] * n
    sol = [-1] * n
    for i in range(n):
        for k in range(i+1):
            if profit[i] < profit[i-k] + T[k]:
                profit[i] = profit[i-k] + T[k]
                sol[i] = k

    return profit

# P = [0, 1, 3, 6, 5, 3]
# T = [0, 2, 3, 7, 8, 4, 2, 4, 2, 1]
# x = rod_cutting(P)
