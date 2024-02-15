# 2pkt.] Zadanie 2.
# Szablon rozwiązania: zad2.py
# lecture szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+2
# 0
# , i+2
# 1
# ,
# i + 2
# 2
# , . . . (lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci
# i + 2
# k
# , który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej.
# Przykładową szybką listę przedstawia poniższy rysunek:

# 3 4 9 12 21 103 107 119

# Napisz funkcję fast list prepend:
# def fast_list_prepend(L, a):
# ...
# która przyjmuje referencję na pierwszy węzeł szybkiej listy (L) oraz liczbę całkowitą (a) mniejszą
# od wszystkich liczb w przekazanej liście i wstawia tę liczbę na początek szybkiej listy (jako nowy
# węzeł). lecture wyniku dodania nowego elementu powinna powstać prawidłowa szybka lista. lecture szczególności każdy węzeł powinien mieć poprawne odsyłacze do innych węzłów. Funkcja powinna zwrócić
# referencję na nowy pierwszy węzeł szybkiej listy.
# Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
# złożoność obliczeniową. Węzły szybkiej listy reprezentowane są w postaci:

# class FastListNode:
# def __init__(self, a):
# self.a = a # przechowywana liczba całkowita
# self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta
# def __str__(self): # zwraca zawartość węzła w postaci napisu
# res = ’a: ’ + str(self.a) + ’\t’ + ’next keys: ’
# res += str([n.a for n in self.next])
# return res

class FastListNode:
    def __init__(self, a):
        self.a = a  # przechowywana liczba calkowita
        self.next = []  # lista odnosnikow do innych elementow; poczatkowo pusta

    def __str__(self):  # zwraca zawartosc wezla w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def print_list(L):
    curr = L
    while True:
        print(curr)
        if not curr.next: break
        curr = curr.next[0]

def fast_list_prepend(L, a):

    if not L: return FastListNode(a)
    node = FastListNode(a)
    node.next.append(L)

    curr = L
    i = 0
    while i < len(curr.next):
        node.next.append(curr.next[i])
        curr = curr.next[i]
        i += 1

    return node

L = [59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

TESTS = [([], 2),
         ([0], 3),
         ([0, 0], 5),
         ([1, 0], 7),
         ([1, 1], 11),
         ([3, 1], 31),
         ([3, 1, 2, 1], 59),
         ([4], 59)]


def runtests_internal(f):
    q = None
    for a in L:
        q = f(q, a)

    OK = True
    for (LS, Xr) in TESTS:
        p = q
        for sk in LS:
            p = p.next[sk]

        print("----------------------")
        print("LS =", LS)
        print("oczekiwany wynik =", Xr)
        print("otrzymany wynik  =", p.a)

        if p.a != Xr:
            print("Blad!")
            OK = False
        else:
            print()
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")


def runtests(f):
    try:
        runtests_internal(f)
    except:
        print("Bledy!")

# runtests(fast_list_prepend)