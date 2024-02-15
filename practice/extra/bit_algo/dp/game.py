# Dostajemy listę wartosci. Gramy z drugim graczem. Wybieramy
# zawsze jedna wartosc z jednego z koncow tablicy i dodajemy do swojej sumy
# a nastepnie to samo robi nasz przeciwnik. Zakladajac, ze przeciwnik
# gra optymalnie, jaka maksymalna sumę mozemy uzbierac? (Uogolniony problem
# paczki mentosow)

# f(i, j) - moja maksymalna wartosc gry od i do j, maksymalna wartosc gry przeciwnika (ja zaczynam)
# f(i,i) = T[i], 0

# Tushar Roy - optimal strategy game :))

def game(T):

    n = len(T)
    dp = [[[float("-inf"), float("-inf")] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = [T[i], 0]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):

            if dp[i][j][0] < T[i] + dp[i+1][j][1]:
                dp[i][j] = [T[i] + dp[i+1][j][1], dp[i+1][j][0]]
            if dp[i][j][0] < T[j] + dp[i][j-1][1]:
                dp[i][j] = [T[j] + dp[i][j-1][1], dp[i][j-1][0]]

    print("my max profit is", dp[0][n-1][0])
    print("max opponent profit is", dp[0][n-1][1])
    return dp[0][n-1][0]

T = [3, 9, 1, 2]
# game(T)