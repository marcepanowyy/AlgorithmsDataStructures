from egz1atesty import runtests

def snow(S):

    S.sort(reverse=True)

    i, days, res = 0, 0, 0

    while S[i] - days > 0:
        res += S[i]
        res -= days
        i += 1
        days += 1

    return res

S = [1, 7, 3, 4, 1]
snow(S)

# runtests(snow, all_tests=True)

