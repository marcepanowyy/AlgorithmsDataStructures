# Problem wydawania monet

# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju
# oraz kwote p. Prosze podac algorytm, ktory oblicza ilosc monet potrzebna
# do wydania kwoty T (algorytm zachlanny wydajacy najpierw najwieksza monete
# nie dziala: dla monet 1, 5, 8 wyda kwote 15 jako 8+5+1+1 zamiast 5+5+5)

# mozna zrobic w nlogn z wyszukiwaniem binarnym

def coin_ex(M, p):

    n = len(M)
    min_coins = [float("inf")] * (p+1)
    min_coins[0] = 0
    for i in range(p+1):

        for m in M:
            if i-m >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i-m]+1)

    print(min_coins)
    return min_coins[p]

M = [1,5,8]
p = 15

coin_ex(M, p)
