from kol2btesty import runtests

# O(n**2)

def min_cost(O, C, T, L):

    n = len(O)
    dp = [[float("inf")] * 2 for _ in range(n+2)]
    dp[0][0] = 0
    dp[0][1] = 0

    lots = [(0, 0)]
    for i in range(n):
        lots.append((O[i], C[i]))

    lots.append((L, 0))

    lots.sort(key=lambda x: x[0])

    for i in range(n+2):

        curr_dist = lots[i][0]

        curr_price0 = dp[i][0]   # 1*T
        add_dist0 = T

        curr_price1 = dp[i][1]   # 2*T
        add_dist1 = 2 * T

        for j in range(i+1, n+2):

            parking_lot_distance = lots[j][0]
            parking_lot_price = lots[j][1]

            if curr_dist + add_dist0 >= parking_lot_distance:
                dp[j][1] = min(dp[j][1], curr_price1 + parking_lot_price)     # wykonujemy skok z pola z pola z ktorego wykonalismy 2*T
                dp[j][0] = min(dp[j][0], curr_price0 + parking_lot_price)     # wykonujemy zwykly skok ze zwyklego pola

            if curr_dist + add_dist1 >= parking_lot_distance:
                dp[j][1] = min(dp[j][1], curr_price0 + parking_lot_price)     # wykonujemy podwojny skok
            else: break

    # return min(dp[-1])
    print(*dp, sep='\n')

# runtests( min_cost, all_tests = True )

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

min_cost(O, C, L, T)