# Czarodziej Pascal ma N stosów porcelanowych talerzy, przy czym
# kazdy stos zawiera dokladnie k talerzy. Pascal wystawia dzis
# wieczorem kolacje dla P gosci i jedzenie bedzie serwowane na tych
# wlasnie talerzach. Kazdy talerz ma pewne piekno okreslone
# liczba calkowita. Pomoz czarodziejowi wybrac dokladnie P talerzy
# tak, by mialy one maksymalne mozliwe piekno. Ale uwaga! Stos to stos
# wiec jesli chcesz zabrac jakis talerz, to musisz zabrac wszystkie nad nim.

# f(i,k) - maksymalna pieknosc dla i talerzy z k pierwszych stosow

# f(i,k) = max po j {0, ..., i} z f(i-j, k-1)

from copy import deepcopy

def get_arr_sum(S):
    n = len(S)
    k = len(S[0])
    sum_arr = deepcopy(S)
    for i in range(n):
        for j in range(1, k):
            sum_arr[i][j] += sum_arr[i][j-1]
    return sum_arr


def pascal_wizard(S, P):

    n = len(S)
    k = len(S[0])
    sum_arr = get_arr_sum(S)
    dp = [[0] * (P + 1) for _ in range(n)]

    for j in range(1, min(P, k) + 1):         # warunki brzegowe
        dp[0][j] = sum_arr[0][j-1]

    for i in range(1, n):                     # stosy 1 ,..., n-1
        for j in range(1, P+1):               # talerze 1, ..., p
            dp[i][j] = dp[i-1][j]
            for t in range(1, min(j, k)+1):   # bierzemy najlepszy wybor na i-1 i teraz tak:co by bylo gdybysmy wzieli jeden talerz ze stosu i oraz jeden mniej talerz z najlepszego wyboru i-1 itp.
                # a = dp[i - 1][j - t]        # najlepszy poprzedni wybor bez t talerzy
                # b = sum_arr[i][t-1]         # wybor z t nowymi talerzami z nowego stosu
                dp[i][j] = max(dp[i][j], dp[i-1][j-t] + sum_arr[i][t-1])

    print(dp[n-1][P])
    return dp[n-1][P]

S1 = [[1,2,1],[8,1,1],[3,7,1]]
P1 = 4
pascal_wizard(S1, P1)

