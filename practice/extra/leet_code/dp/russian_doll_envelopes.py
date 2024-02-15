# Russian Doll Envelopes

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

from bisect import bisect_left

def russian(envelopes):

    envelopes.sort(key=lambda x: (x[0], -x[1]))
    res = []

    for _, h in envelopes:
        l, r = 0, len(res) - 1

        # find the insertion point in the Sort order

        while l <= r:
            mid = (l + r) // 2
            if res[mid] >= h:
                r = mid - 1
            else:
                l = mid + 1

        idx = l
        if idx == len(res):
            res.append(h)
        else:
            res[idx] = h

    return len(res)

