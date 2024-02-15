# Dane sa lampki o numerach od 0 do n-1. Kazda z nich moze swiecic na zielono, czerwono lub niebiesko i ma jeden przelacznik, ktory zmienia jej kolor z zielonego na czerwony
# z czerwonego na niebieski i z niebieskiego na ziekony. Poczatkowo wszystkie lampki swieca na zielono. Operacja (a,b) oznacza wcisniecie przelacznika na kazdej z lampek o numerach
# od a do b. Wykonanych bedzie m operacji . Prosze napisac fukcje

# def lamps(n, L)

# ktora majac dana liczbe n lampek oraz liste L operacji (wykonywanych w podanej kolejnosci) zwraca ile maksymalnie lampek swiecilo sie na niebiesko)
# niestety slabsza zlozonosc (dostalbym 3,5 na 6)

# przyklad. Wywolanie lamps(8, [(0,4), (2,6)] powinno zworic liczbe 3. Poczatkowo wszystkie lampki o numerach od 0 do 7 swieca na zielono. Nastepnie lampki o numerach od 0 do 4
# zmieniaja kolor na czerwony. Po ostatniej operacji lampki o numerach od 2 do 4 zmieniaja kolor na niebieski, a lampki 5 i 6 zmieniaja kolor na czerwony

# from zad3testy import runtests

def lamps(n, L):

    lights = [0] * n      # 0 means green, 1 means red, 2 means blue

    max_ = 0
    counter = 0

    for a, b in L:

        while a != b+1:

            lights[a] += 1
            lights[a] %= 3

            if lights[a] == 2:
                counter += 1
            elif lights[a] == 0:
                counter -= 1

            a += 1

        max_ = max(max_, counter)

    return max_


runtests(lamps)

# print(lamps(10, [(0, 4), (2, 6), (1, 6), (2, 5), (7, 9), (1, 7), (1, 7), (1, 7)]))




