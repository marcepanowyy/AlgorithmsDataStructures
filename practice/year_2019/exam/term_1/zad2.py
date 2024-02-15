# Zad.2
# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
# być zarówno dodatnie jak i ujemne):
# n1 + n2 + ... + nk
# Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
# kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
# dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
# najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
# wybiera kolejność dodawań.
# Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
# bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
# wejściowej:
# [1,−5, 2]
# funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji opt sum powinien mieć postać:
# def opt_sum(tab):
# ...

# -5 + 2 = -3   (3)
# -3 +1 = -2    (2)

from zad2testy import runtests


# Jest to przykład algorytmu zachłannego.
# Dla każdego ciągu liczb szukamy najmniejszej wartości tymczasowej, wybieramy ją, dodajemy elementy i powtarzamy proces
# aż do uzyskania wyniku końcowego. Zapamiętujemy największą z obliczonych wartości tymczasowych (tj. bierzemy max).

# Przeszukiwanie tablicy w celu znalezienia najmniejszej wartości tymczasowej zajmuje O(n)
# Rekurencja ma głębokość O(n)
# Zatem złożoność algorytmu to O(n)*O(n) = O(n^2)

# Algorytm działa zachłannie, ponieważ wybieramy wynik lokalnie najlepszy.
# Aby pokazać, że algorytm jest poprawny, udowodnijmy najpierw jego słuszność dla k = 3
# Zakładamy BSO, że idealne dodawanie to n1+n2, a dopiero potem (n1+n2)+n3
# Nasz algorytm wybiera n2+n3, a później n1+(n2+n3)
# Zakładamy również, że abs(n1+n2) >= abs(n2+n3) (przez sprzeczność)

# Zauważamy, że największą wartością tymczasową może tutaj być jedynie jeden z wybranych wyników.
# Jeżeli to końcowy jest największy, to nasz algorytm spisał się tak samo dobrze jak wzorcowy, bo dodawanie jest przemienne
# ( tj. n1 + n2= n3 = (n1 + n2) + n3 = n1 + n2 + n3) )
# Jeżeli z kolei to pierwszy wynik tymczasowy jest większy od drugiego, to z założenia widzimy,
# że wybraliśmy mniejszą bądź równą wartość w porównaniu z tą wzorcową,
# więc nasz algorytm pokazuje rozwiązanie niegorsze od wzorcowego, czyli jest poprawny.

# Rozszerzamy to do 4 elementów
# Jeżeli maksymalna wartość tymczasowa nie jest wartością końcową ani nie sumuje elementu 4, to nasz algorytm działa poprawnie,
# co udowodniono wyżej (założenie indukcyjne)
# Jeżeli maksymalna wartość tymczasowa zawiera składnik n4, to nasz algorytm w którymś zejściu rekurencyjnym wskaże tę wartość.
# Zakładamy, że się pomylił. Wtedy istnieje rozwiązanie różne od wskazanego przez algorytm. Jak się jednak okazuje, we wzorcowym
# rozwiązaniu, w pewnym momencie wystąpiłaby wartość tymczasowa większa lub równa od wybranej (ze względu na przemienność dodawania).
# Nie może być większa, bo to byłaby sprzeczność, może być co najwyżej równa.
# lecture tym wypadku nasz algorytm wskazał niegorszą odpowiedź od wzorowej.

# Podobnie można uogólnić rozumowanie do k-składnikowej sumy. Zatem algorytm zachłanny jest poprawny dla k liczb naturalnych.


def prepTabCopy(tab, i):
    newVal = tab[i]+tab[i+1]
    tabCP = tab[:]  #kopiowanie tablicy, aby nie naruszyć jej struktury (O(n))

    tabCP[i] = newVal   #wstawienie nowej wartości
    del tabCP[i+1]      #usunięcie elementu

    return tabCP


def opt_sum(tab):
    if len(tab) == 1:       #przypadek bazowy - sprawdzamy wynik końcowy
        return tab[0]

    # lowestAbsolute - największy wynik tymczasowy; ansInd - indeks pierwszego z dwóch elementów, który ten wynik tworzy.
    # Na poczatek zakładamy, że to pierwsza para elementów jest tą, którą szukamy

    lowestAbsolute = abs(tab[0] + tab[1])
    ansInd = 0

    #przeszukiwanie tablicy w poszukiwaniu najmniejszej wartości bezwzględnej
    for i in range(1, len(tab) - 1):
        tmp = abs(tab[i]+tab[i+1])
        if tmp < lowestAbsolute:
            lowestAbsolute = tmp
            ansInd = i

    # przygotowanie tablicy po dodaniu dwóch elementów o najmniejszej wartości bezwzględnej po zsumowaniu
    prepTab = prepTabCopy(tab, ansInd)

    # sprawdzamy rekurencyjnie, czy pozostałe dodawania nie mają większej wartości tymczasowej
    # max(a1,a2,a3...) = max(a1, max(a2, max(a3,...)))
    return max(lowestAbsolute, opt_sum(prepTab))

# runtests(opt_sum)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# moje ulomne rozw w czasie O(n**3)
# f(i, j) - optymalna suma od indeksu i do indeksu j
# f(i, i) = 0
# f(i, i+1) = abs(T[i] * T[i+1])
# f(i, j) = min{f(i,j), max{abs(g(i,k)+g(k+1,j), f(i,k), f(k+1,j)}}, gdzie g(i, j) to aktualna rzeczywista suma


def optimal_sum(T):

    n = len(T)
    dp = [[float("inf")] * n for _ in range(n)]
    act_sum = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
        act_sum[i][i] = T[i]
    for i in range(n-1):
        act_sum[i][i+1] = T[i] + T[i+1]
        dp[i][i+1] = abs(T[i] + T[i+1])

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i, j):
                curr_value = act_sum[i][k] + act_sum[k+1][j]
                if dp[i][j] > min(dp[i][j], max(dp[i][k], dp[k+1][j], abs(curr_value))):
                    dp[i][j] = min(dp[i][j], max(dp[i][k], dp[k+1][j], abs(curr_value)))
                    act_sum[i][j] = act_sum[i][k] + act_sum[k+1][j]

    return dp[0][n-1]

# runtests(optimal_sum)



