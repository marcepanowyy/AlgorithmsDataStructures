# Dostajac na wejsciu string zlozony z liter a-z, zwroc najdluzszy jego fragment
#, ktory jest palindromem

# podobne do palindromic substrings z leet_code

def get_max_odd(str):
    odd = str[0]
    n = len(str)
    for i in range(n):
        left, right = i-1, i+1
        while left >= 0 and right < n and str[left] == str[right]:
            if len(odd) < len(str[left:right+1]):
                odd = str[left:right+1]
            left -= 1
            right += 1
    return odd

def get_max_even(str):
    even = 'a'
    n = len(str)
    for i in range(1, n):
        left, right = i-1, i
        while left >= 0 and right < n and str[left] == str[right]:
            if len(even) < len(str[left:right+1]):
                even = str[left:right + 1]
            left -= 1
            right += 1

    if len(even) != 1: return even
    return None

def get_solution(str):
    max_odd = get_max_odd(str)
    max_even = get_max_even(str)
    if max_even == None or len(max_odd) > len(max_even):
        return max_odd
    return max_even

str = 'wwwwweepipeewokookokooommoo'
# print(get_solution(str))