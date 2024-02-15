# Opis: 
# (0) Tworzymy tablicę z maksymalną ilością złota, jakie możemy uzyskać będąc w danej komnacie. 
#     Uzupełniamy ją początkowymi wartościami.
# (1) Zaczynamy od pierwszej komnaty i obliczamy ile złota nam maksymalnie zostanie jeśli przejdziemy przez osiagalne komnaty. 
#     Wartości wpisujemy dla odpowiadającyh komnatom elementów tablicy.
# (2) Przechodzimy następnie (liniowo) przez pozostałe komnaty i powtarzamy czynność. Jeżeli dla danej komnaty już uzupełniliśmy wartość,
#     wybieramy maksymalną wartość. Nie obchodzi nas potem, jaką drogą dotarliśmy do danej komanty, ważne, że uzbieraliśmy daną ilość złota.

# Złożoność: O(n)

from egz2btesty import runtests

def magic_old(C):
    n = len(C)
    tab = [None for _ in range(n)]
    tab[0] = 0
    for i in range(n):
        gold = C[i][0]
        for j in range(1, 4):
            if C[i][j][1] == -1:
                continue

            hand = tab[i]
            if hand is None:
                continue
            if gold == C[i][j][0]:
                pass
            elif gold > C[i][j][0]:
                diff = gold - C[i][j][0]
                if diff > 10:
                    continue
                else:
                    hand += diff
            elif gold < C[i][j][0]:
                diff = C[i][j][0] - gold
                if diff > hand:
                    continue
                else:
                    hand -= diff

            if tab[C[i][j][1]] is None:
                tab[C[i][j][1]] = hand
            else:
                tab[C[i][j][1]] = max(tab[C[i][j][1]], hand)

    if tab[-1] is None:
        return -1
    else:
        return tab[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(magic_old, all_tests=True)

