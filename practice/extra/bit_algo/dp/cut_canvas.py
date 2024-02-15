# Dany jest prostokatny kawalek tkaniny o wymiarach X na Y oraz lista n produktów
# ktore moga zostac wykonane z tej tkaniny. Do wytworzenia kazdego produktu
# i (i zmienia sie od 1 do n) potrzebny jest prostokatny kawalek tkaniny o wymiarach
# ai na bi, a zysk ze sprzedazy produktu wynosi ci. Zakladamy, ze ai, bi, ci sa
# dodatnie calkowite. Majac maszyne, ktora moze rzeciac dowolny prostokatny kawalek
# tkaniny na dwa kawalki wzduz linii poziomej lub pionowej, zaprojektuj algorytm,
# ktory wyznaczy taka strategie ciecia materialu o wymiarach X na Y, aby sprzedaz
# wytworzonych produktow dala lacznie jak najwiekszy zysk

def cut_canvas(P: 'array of profits', x: 'width of the canvas', y: 'height of the canvas'):
    F = [[-1] * (x + 1) for _ in range(y + 1)]

    def cut(i, j):
        if i == 0 or j == 0:
            F[i][j] = 0
        if F[i][j] < 0:
            F[i][j] = P[i][j]
            # Cut horizontally into two parts
            for h in range(1, i // 2 + 1):
                F[i][j] = max(F[i][j], cut(h, j) + cut(i - h, j))
            # Cut vertically into two parts
            for w in range(1, j // 2 + 1):
                F[i][j] = max(F[i][j], cut(i, w) + cut(i, j - w))
        return F[i][j]

    return cut(y, x)

X = 10
Y = 10
S = [(3,3), (4,2), (5,4), (10, 10), (7,7), (3,12), (2,8)]
P = [100, 100, 50, 10, 1000, 1000, 1000, 1000]
cut_canvas()

P = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]