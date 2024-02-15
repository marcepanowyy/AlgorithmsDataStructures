# You are given N identical eggs and you have access to a K-floored building from 1 to K.

# There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break,
# and any egg dropped at or below floor f will not break. There are few rules given below.

# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.

# Tushar Roy cool guy

# Input:
# N = 1, K = 2
# Output: 2
# Explanation:
# 1. Drop the egg from floor 1. If it
#    breaks, we know that f = 0.
# 2. Otherwise, drop the egg from floor 2.
#    If it breaks, we know that f = 1.
# 3. If it does not break, then we know f = 2.
# 4. Hence, we need at minimum 2 moves to
#    determine with certainty what the value of f is.

# if: egg > floor dp[egg][floor] = dp[egg-1][floor]
# else: dp[egg][floor] = min((max(dp[egg-1][k-1], dp[egg][floor-k])+1, dp[egg][floor]), k = {1,...,floor}

def egg_dropping(floors, eggs):

    dp = [[float("inf")] * (floors+1) for _ in range(eggs+1)]

    for floor in range(floors+1):                             # Warunki poczatkowe
        dp[0][floor] = 0
    for egg in range(eggs+1):                                 # Warunki poczatkowe
        dp[egg][0] = 0
    for floor in range(1, floors+1):                          # Warunki poczatkowe
        dp[1][floor] = dp[1][floor-1] + 1
    for egg in range(1, eggs+1):                              # Warunki poczatkowe
        dp[egg][1] = 1

    for egg in range(2, eggs+1):
        for floor in range(1, floors+1):

            if egg > floor:
                dp[egg][floor] = dp[egg - 1][floor]

            else:
                for k in range(1, floor+1):
                    curr_value = dp[egg][floor]
                    breaks = dp[egg-1][k-1]
                    # doesnt_break = dp[egg][floor-k] if floor != k else 0
                    doesnt_break = dp[egg][floor-k]
                    dp[egg][floor] = min(dp[egg][floor], max(breaks, doesnt_break) + 1)

                    # jesli jajko sie stlucze, to musimy sprawdzic k-1 poziomow majac egg-1 jajek
                    # jesli sie nie stlucze, to musimy sprawdzic floor-k poziomow majac egg jajek XD

    # print(*dp, sep = "\n")
    print(dp[eggs][floors])
    return dp[eggs][floors]


egg_dropping(6, 2)
egg_dropping(10, 2)

