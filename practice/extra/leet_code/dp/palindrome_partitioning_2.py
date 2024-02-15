# PalindromePartitioningII

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

def get_palindrome_arr(s):

    n = len(s)
    arr = [[False] * n for _ in range(n)]

    i = 0
    while i < n:                            # odd palindrome
        l, r = i, i
        while 0 <= l and r < n:
            if s[l] == s[r]:
                arr[l][r] = True
                l -= 1
                r += 1
            else: break

        i += 1

    i = 0
    while i < n-1:                          # even
        l, r = i, i+1
        while 0 <= l and r < n:
            if s[l] == s[r]:
                arr[l][r] = True
                l -= 1
                r += 1
            else: break
        i += 1

    return arr

def palindrome_part2(s):

    n = len(s)
    arr = get_palindrome_arr(s)
    min_cuts = [float("inf")] * n              # min_cuts(i) - minimalna ilosc ciec do i-tego indeksu
    min_cuts[0] = 0

    for i in range(1, n):
        if arr[0][i]: min_cuts[i] = 0
        else:
            for j in range(i):
                if arr[j+1][i] and min_cuts[j] + 1 < min_cuts[i]:
                    min_cuts[i] = min_cuts[j] + 1

    return min_cuts[n-1]


s1 = 'caa'
s2 = 'aab'
s3 = "efe"
s4 = "eefe"
s5 = "ee"
s6 = "eefee"
s7 = "saafaa"

# print(palindrome_part2(s1))
# print(palindrome_part2(s2))
# print(palindrome_part2(s3))
# print(palindrome_part2(s4))
# print(palindrome_part2(s5))
# print(palindrome_part2(s6))
print(palindrome_part2(s7))