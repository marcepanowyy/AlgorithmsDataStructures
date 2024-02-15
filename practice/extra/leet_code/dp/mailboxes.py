# Given the array houses where houses[i] is the location of the ith house along a
# street and an integer k, allocate k mailboxes in the street.

# Return the minimum total distance between each house and its nearest mailbox.

# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.

# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5

# dp(i, k) - minimalny calkowita odleglosc od 0 do itego domu majac k mailboxes to obstawienia

def allocate_mailboxes(houses, k):

    houses.sort()
    n = len(houses)

    dp = [[float("inf")] * n for _ in range(k+1)]

    distance = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            mid = houses[(i+j)//2]
            for h in range(i, j+1):
                distance[i][j] += abs(mid - houses[h])          # distance[i][j] - dystans od i do j stawiajac jeden mailbox

    for idx in range(n):                                        # jesli mamy tyle mailboxow ile k, to
        for mailbox in range(idx+1, k+1):                       # rozw jest 0
            dp[mailbox][idx] = 0

    for i in range(n):
        dp[1][i] = distance[0][i]

    for a in range(n):
        for mailbox in range(1, k+1):
            for b in range(a):
                actual_value = dp[mailbox][a]
                one_less_mailbox = dp[mailbox-1][b]
                dist_value = distance[b+1][a]
                dp[mailbox][a] = min(actual_value, one_less_mailbox + dist_value)


    return dp[k][n-1]


houses1 = [3,6,14,10]
k1 = 4
# Expected: 0

houses2 = [1,8,12,10,3]
k2 = 3
# Expected: 4

houses3 = [1,3,13,7,6]
k3 = 2
# Expected: 9

houses4 = [8,14,20,23,4,25]
k4 = 3
# Expected: 9

houses5 = [1,4,8,10,20]
k5 = 3
# Expected: 5

# print(allocate_mailboxes(houses1, k1))
# print(allocate_mailboxes(houses2, k2))
# print(allocate_mailboxes(houses3, k3))
# print(allocate_mailboxes(houses4, k4))
# print(allocate_mailboxes(houses5, k5))

