# Candy

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.

# Return the minimum number of candies you need to have to distribute the candies to the children.


def candy(ratings):

    n, ans = len(ratings), 0

    dp_prefix = [1 for _ in range(n)]
    dp_sufix = [1 for _ in range(n)]

    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            dp_prefix[i] = dp_prefix[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            dp_sufix[i] = dp_sufix[i+1] + 1

    for i in range(n):
        ans += max(dp_prefix[i], dp_sufix[i])

    return ans

ratings1 = [1, 0, 2]

print(candy(ratings1))