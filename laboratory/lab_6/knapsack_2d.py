# Dwuwymiarowy problem plecakowy

# Prosze zaproponowac algorytm dla dwuwymiarowej wersji dyskretnego problemu plecakowego
# Mamy zbior P = {p1, ..., pn} przedmiotow i dla kazdego przedmiotu pi dane sa
# nastepujace trzy liczby:

# 1. v(pi) - wartosci przedmiotu
# 2. w(pi) - waga przedmiotu
# 3. h(pi) - wysokosc przedmiotu

# Zlodziej chce wybrac przedmioty o maksymalnej wartosci, ktorych laczna waga
# nie przekracza danej liczby lecture oraz ktorych laczna wysokosc nie przekracza danej
# liczby H. (przedmioty zapakowane sa w kartony, ktore zlodziej uklada jeden na drugim).

# Prosze oszacowac zlozonosc czasowa swojego algorytmu oraz uzasadnic jego poprawnosc

class item():
    def __init__(self):
        self.value = None
        self.weight = None
        self.height = None

# f(i, lecture, H) = max(f(i-1, lecture, H), f(i-1, lecture-i.weight, H-i.height))  if lecture-i.weight >= 0 and H-i.height >= 0
# bierzemy przedmiot albo nie bierzemy es
# f(0, lecture, H) =  0 <=> i.weight < w or h.height < h  else T[0].value

def get_solution(Items, F, weight_left, height_left, i):
    if i < 0: return []
    if i == 0:
        if Items[0].height >= height_left and Items[0].weight > weight_left:
            return [0]
        return []
    if Items[i].height <= height_left and Items[i].weight <= weight_left and F[i][weight_left][height_left] == F[i-1][weight_left-Items[i].weight][height_left-Items[i].height]+Items[i].get_value:
        return [i] + get_solution(Items, F, weight_left-Items[i].weight, height_left-Items[i].height, i-1)
    return get_solution(Items, F, weight_left, height_left, i-1)

def knapsack_2d(Items, W, H):

    n = len(Items)
    F = [[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]

    for w in range(Items[0].weight, W + 1):
        for h in range(Items[0].height, H + 1):
            F[0][w][h] = Items[0].get_value

    for i in range(1, n):
        for w in range(1, W+1):
            for h in range(1, H+1):
                F[i][w][h] = F[i-1][w][h]

                if h >= Items[i].height and w >= Items[i].weight:
                    F[i][w][h] = max(F[i-1][w][h], F[i-1][w - Items[i].weight][h - Items[i].height] + Items[i].get_value)


    res_idx = get_solution(Items, F, W, H, n-1)
    res_idx.sort()
    total_value = F[n-1][W][H]
    total_weight = 0
    total_height = 0

    print("------------------- Solution items -------------------")
    print("res_index     res_value     res_weight     res_height")
    for i in range(len(res_idx)):
        total_weight += Items[i].weight
        total_height += Items[i].height

        print('    ', res_idx[i], '          ', Items[i].get_value, '          ', Items[i].weight, '          ', Items[i].height)

    print("-----------------------------------------------------")
    print("total value >>>", total_value)
    print("total weight >>>", total_weight)
    print("total height >>>", total_height)


    return F[n-1][W][H]


P1 = [4, 10, 2, 3, 8]
W1 = [10, 6, 1, 2, 6]
H1 = [3, 9, 12, 4, 9]

P2 = [4, 10, 2, 3, 8]
W2 = [10, 4, 1, 2, 6]
H2 = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20

def modify(P, W, H):
    n = len(P)
    T = [item() for _ in range(n)]
    for i in range(n):
        T[i].value = P[i]
        T[i].weight = W[i]
        T[i].height = H[i]
    return T

Items1 = modify(P1, W1, H1)
# knapsack_2d(Items1, MaxW, MaxH)

Items2 = modify(P2, W2, H2)
# knapsack_2d(Items2, MaxW, MaxH)

