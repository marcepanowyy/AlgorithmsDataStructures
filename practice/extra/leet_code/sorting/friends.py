# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
#
# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
#
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
#
# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

# Return the total number of friend requests made


def appropriate_age(ages):
    max_ = max(ages)
    age_buckets = [0] * (max_+1)
    for age in ages:
        age_buckets[age] += 1

    age_cum = [age_buckets[0]] * (max_ + 1)
    for i in range(1, len(age_buckets)):
        age_cum[i] = age_cum[i-1] + age_buckets[i]

    ans = 0
    for age in range(1, len(age_buckets)):
        if age_buckets[age]:
            k = int(age * 0.5 +7)
            if k < age:
                ans += age_buckets[age] * (age_cum[age-1] - age_cum[k])
            if age > k:
                ans += age_buckets[age] * (age_buckets[age]-1)
    return ans

def appropriate_age0(T):
    n = len(T)
    requests = 0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if T[i] * 0.5 + 7 >= T[j] or T[i] < T[j] or (T[i] < 100 and T[j] > 100):
                    continue
                else:
                    requests += 1
    return requests

ages = [16,17,18]
print(appropriate_age(ages))