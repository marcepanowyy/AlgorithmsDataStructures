# Ładowanie promu

# Dana jest tablica A[n] z dlugosciami samochodow, ktore stoja w kolejce,
# zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba dlugosci L.
# Prosze napisac program, ktory wyznacza, ktore samochody powinny pojechac
# na ktory pas, zeby zmiescilo sie jak najwiecej aut.
# Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy A

#               { 1, pierwsze i samochodow mozna rozmiescic na promie tak, ze zostaje
# f(i, g, d) =  { g miejsca na gorze i d miejsca na dole
#               { 0, w p.p.

#   max {n | f(n,g,d)=1}
# po n, g, d

# xxxx

# f(l1, l2, T, i) - ile samochodow moze sie zmiescic
# majac l1 miejsca na pierwszym pasie i l2 na drugim
# pasie do itego samochodu wlacznie  ???

# f(l1, l2, T, i) = 0, T[i] > l1 and T[i] > l1
# f(l1 - T[i], l2, T, i + 1) + 1, T[i] > l2
# f(l1, l2 - T[i], T, i + 1) + 1, T[i] > l1
# max(f(l1 - T[i], l2, T, i + 1), f(l1, l2 - T[i], T, i - 1)) + 1 w p.p.

# wynik
# f(l1, l2, T, 0)

