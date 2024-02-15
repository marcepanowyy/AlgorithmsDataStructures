# Alice and Bob continue their games with piles of stones. There are several stones arranged in a row,
# and each stone has an associated value which is an integer given in the array stoneValue.

# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take
# 1, 2, or 3 stones from the first remaining stones in the row.

# The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

# The objective of the game is to end with the highest score, and the winner is the player with the highest
# score and there could be a tie. The game continues until all the stones have been taken.

# Assume Alice and Bob play optimally.
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

# f(i) = max(stone[i:i+k] - dp[i+k]) where k in {1,2,3}

stones1 = [1, -8, -100, 20, 50, 100]
stones2 = [1, -8, -100, 10]

# We first change the problem who is the winner to the maximum score Alice can get.

# Thus, we define a helper function max_score(idx), which computes the maximum score of Alice (more precisely, the first picking player). Then the idea is fairly trivial.

# Generally, take the action that results in minimal scores for Bob, (more precisely, the next picking player)
# if there are only 1 stone left, we have to take it
# if there are only 2 ~ 3 stone left,
# - we can either take all of them
# - or take the action that results in minimal scores for Bob

def stoneGameIII(stoneValue):
    post_sum = [0]
    for s in stoneValue[::-1]:
        post_sum += post_sum[-1] + s,
    post_sum = post_sum[::-1][:-1]
    n = len(stoneValue)

    dp = [float("-inf")] * (n - 3) + post_sum[-3:]
    for i in range(n - 2, -1, -1):
        dp[i] = max(dp[i], post_sum[i] - min(dp[i + j] for j in range(1, 4) if i + j < n))

    alice, bob = dp[0], post_sum[0] - dp[0]
    # print(dp)
    return 'Tie' if alice == bob else 'Alice' if alice > bob else 'Bob'

stoneGameIII(stones1)
