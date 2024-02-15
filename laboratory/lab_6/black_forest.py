# Black forest

# Black forest to las rosnacy na osi liczbowej gdzies w poludniowej Anglii.
# Las sklada sie z n drzew rosnacych na pozycjach 0, ..., n-1. Dl kazdego i
# znany jest zysk c(i), jaki mozna osiagnac scinajac drzewo z pozycji i.
# John Lovenoses chce uzyskac maksymalny zysk ze scinanych drzew, ale prawo
# zabrania scinanani dwoch drzew pod rzad. Prosze zaproponowac algorytm,
# dzieki ktoremu John znajdzie optymalny plan wycinki.

def get_solution(T, max_profit, i, profit):
    if i == 0:
        if profit - T[i] == 0: return [0]
    if i == 1:
        if profit - T[i] == 0: return [1]
        else: get_solution(T, max_profit, i - 1, profit)

    if max_profit[i] - T[i] == max_profit[i - 2]: return [i] + get_solution(T, max_profit, i - 2, profit - T[i])

def black_forest(T):
    n = len(T)
    max_profit = [float("-inf")] * n
    max_profit[0] = T[0]
    max_profit[1] = max(T[0], T[1])
    for i in range(2, n):
        max_profit[i] = max(T[i]+max_profit[i-2], T[i-1])  # biore drezwo albo go nie biore es

    res = get_solution(T, max_profit, n-1, max_profit[n-1])[::-1]
    print("max profit, sir:", max_profit[n-1])
    print("you gotta cut trees at indexes:", res)

    return res

T = [3, 6, 4, 2, 1, 8]
black_forest(T)