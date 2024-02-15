# Mamy dany ciag napisow (slow) S = [s1, ..., sn] oraz pewien napis t.
# Wiadomo, ze t mozna zapisac jako zlaczenie pewnej ilosci napisow z S
# (z powtorzeniami). Na przyklad dla S = ['ab', 'abab', 'ba', 'bab', 'b'] napis
# t = ababbab mozna zapisac miedzy innymi jako s2s4 lub jako s1s1s3s5.
# taki wybor konkretnych si nazywa reprezentacja. Przez szerokosc reprezentacji
# rozumiemy dlugosc najkrotszego si nalezacego do reprezentacji.
# Dla s2s4 szerokosc to 3, a dla s1s1s3s5, szerokosc to 1. Zaimplementuj algorytm
# ktory majac na wejsciu S oraz t znajdzie maksymalna szerokosc reprezentacji t
# (tzn. najkrotszy napis w jej reprezentacji jest najdluzszy)

# O(n**2 * m)

def in_arr(S, str):
    n = len(S)
    for i in range(n):
        if str == S[i]:
            return True
    return False

def get_index(S, str):
    n = len(S)
    for i in range(n):
        if S[i] == str:
            return i
    return None

def get_solution(parents, S, dp, idx):
    if idx < 0: return []
    x = S[parents[idx]]
    return [S[parents[idx]]] + get_solution(parents, S, dp, idx-dp[idx])

def representation(S, t):
    n = len(t)
    dp = [float("-inf")] * n
    parents = [-1] * n
    for i in range(n):
        for j in range(i):
            str = t[j:i+1]
            if in_arr(S, str) and dp[i] < len(str):
                dp[i] = len(str)
                parents[i] = get_index(S, str)

    res = get_solution(parents, S, dp, n-1)
    ans = len(min(res, key=len))
    print("maksymalna szerokosc:", ans)
    print("najlepsze napisy:", res)
    return ans

S1 = ['ab', 'abab', 'ba', 'bab', 'b']
t1 = 'ababbab'

S2 = ['ab', 'abab', 'ba', 'bab', 'b']
t2 = 'abababababababab'

# representation(S1, t1)
# representation(S2, t2)
