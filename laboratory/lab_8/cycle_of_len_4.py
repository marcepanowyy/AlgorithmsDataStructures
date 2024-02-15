# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza czy
# w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest
# przez macierz sasiedztwa A.

# nie moj kod XD

def four_length_cycle(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if i != j:
                count = 0
                result = []
                for k in range(n):
                    if k != j and k != i:
                        if graph[i][k] == 1 and graph[j][k] == 1:
                            count += 1
                            result.append(k)
                        if count >= 2:
                            result.append(i)
                            result.append(j)
                            return True, result
    return None, None


graph = [[0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0]]

decision, result = four_length_cycle(graph)
print(decision)
print(result)