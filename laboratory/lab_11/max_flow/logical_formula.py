# Dana jest formuła logiczna postaci: C1 ∧ C2 ∧ ... ∧ Cm, gdzie każda C[i] to klauzula będąca
# alternatywą zmiennych i/lub ich zaprzeczeń. Wiadomo, że każda zmienna występuje w formule dokładnie
# dwa razy, raz zanegowana i raz niezanegowana. Na przykład podana formuła stanowi dopuszczalne
# wejście: (x ∨ y ∨ z) ∧ (~y ∨ w) ∧ (~z ∨ v) ∧ (~x ∨ ~w) ∧ (~v). Proszę podać algorytm, który oblicza
# takie wartości zmiennych, że formuła jest prawdziwa.

# Rozwiązanie:

# Budujemy graf dwudzielny, którego jedną grupą wierzchołków są niezanegowane zmienne występujące
# w formule oraz drugą grupą są formuły C1, C2, C3, .... Następnie łączymy krawędzią każdą zmienną
# z formułą, w której występuje (zanegowana lub niezanegowana). Dzięki temu otrzymujemy graf
# (dwudzielny), którego wierzchołki w zmiennych mają stopień 2, bo każda zmienna występuje dokładnie
# 2 razy (raz zanegowana i raz niezanegowana). Na tak zbudowanym grafie (dwudzielnym) szukamy
# maksymalnego skojarzenia przy pomocy max flow. Jeśli maksymalne skojarzenie jest równe ilości
# zmiennych, to oznacza, że istnieje takie wartościowanie, że formuła jest spełniona. Aby określić
# wartościowanie wszystkich zmiennych należy w powstałym maksymalnym skojarzeniu sprawdzić, do której
# formuły jest skierowana krawędź z wierzchołka zmiennej (czy ma zanegowaną wartość, czy nie). Jeśli
# krawędź wskazuje na formułę, w której jest zanegowana wartość, to przypisujemy jej 0, w przeciwnym razie 1.
# Rozwiązanie to jest poprawne, ponieważ w maksymalnym skojarzeniu może być maksymalnie jedna krawędź
# wychodząca z danej zmiennej, czyli niemożliwe jest, aby któraś zmienna miała przypisaną wartość
# 0 lub 1.


# np dla (x ∨ y) ∧ (~x) ∧ (~y)
#          C1       C2     C3


#     x               C1
#    /                  \
#   X                    \
#  / \                    \
# /   ~x                   \
# s                   C2 -- t
#  \   y                   /
#   \ /                   /
#    Y                   /
#     \                 /
#      ~y              C3

# kazda krawedz jest skierowana z waga 1
# laczymy literały z klauzulami ktore je zawieraja (x polaczymy z C1, y polaczymy z C1, itp.)

# odpalamy algorytm dla sieci przeplywowych z s do t
# jezeli przeplyw jest rowny tyle ile jest klauzuli, to znalezlismy rozwiazanie



# drugie rozwiazanie:
# po lewej stronie tworzymy niezanegowane literaly x, y, ...
# po prawej klauzule C1, C2, ...
# laczymy literaly z klauzulami (nawet jesli wystepuja w nich przeczenia

# np dla (x ∨ y) ∧ (~x) ∧ (~y)

# x polaczymy z C1, C2
# y polaczymy z C1, C3

# szukamy maksymalnego skojarzenia w tym grafie
# jesli rozmiar maksymalnego skojarzenia wynosi tyle ile ilosc klauzuli, to znalezlismy rozwiazanie



# trzecie rozwiazanie (czas liniowy)
# klauzule to wierzcholki w naszym grafie (krawedzie to zmienne)
# jesli jakas zmienna wystepuje w obu klauzulach to laczymy
# wierzcholki krawedzia
# formula jest spelniona wtedy, gdy mozemy nadac orientacje
# krawedzia, ze do kazdego wierzcholka wchodzi przynajmniej
# jedna krawedz

# wybieramy dowolny wierzcholek, puszczamy dfs
# jesli znajdziemy cykl to orientujemy krawedzie
# tak zeby szly po tym cyklu przeszly
# traktujemy cykl jako jeden wierzcholek
# uruchamiamy dfs z tego "wierzcholka"

# gdyby graf bylby drzewem to formula jest niespelnialna