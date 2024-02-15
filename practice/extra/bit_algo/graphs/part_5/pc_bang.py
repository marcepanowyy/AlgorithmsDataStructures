# Kafejka internetowa

# lecture kafejce internetowej jest K komputerow i A aplikacji na plytach CD. Na kazdym
# komputerze moze byc zainstalowana maksymalnie jedna aplikacja. Kazda aplikacja ma
# liste komputerow na ktorych moze dzialac, a na pozostalych nie moze z powodu wymagan
# sprzetowych. Jestes wlascicielem kafejki i wiesz, ilu klientow (mozliwie zero) bedzie
# chcialo jutro skorzystac z danej aplikacji. Zakladamy, ze kazdy klient zajmuje komputer
# na caly dzien.

# Jaka aplikacje powinienes zainstalowac na kazdym z komputerow, aby wszyscy klienci
# mogli skorzystac z tej aplikacji, ktora chca? Jezeli takie przyporzadkowanie nie
# istnieje, algorytm powinien to stwierdzi.

# tworzymy graf skierowany Aplikacja -> Komputer, na ktorym dziala z waga 1

# bedzie to graf dwudzielny

# szukamy maksymalnego skojarzenia (superzrodlo, superujscie)

# Krawedzie wychodzace do zrodla do wierzcholkow ktore oznaczaja aplikacje
# beda mialy wage taka, ile klientow bedzie chcialo z nich skorzystac

# jesli maksymalny przeplyw jest rowny liczbie klientow, to znaczy ze znalezlismy rozwiazanie

