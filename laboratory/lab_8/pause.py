# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce. Jednym z głównych
# elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które tworza spójny graf
# połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo
# zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu działajacych stacji
# mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm podający
# kolejność wyłączania stacji.

# To samo zadanie, tylko inna treść:
# Dany jest spójny graf nieskierowany G = (V,E). Proszę zaproponować algorytm, który znajdzie taką
# kolejność usuwania wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie przestaje
# być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie dotykające go krawędzie).

from queue import Queue

# bfs z zapisywaniem odleglosci

def pause(G):
    n = len(G)
    visited = [False] * n
    dist = [float("inf")] * n

    visited[0] = True
    dist[0] = 0
    res = [0]

    q = Queue()
    q.put(0)                    # zaczynamy od wierzcholka 0 bo nie mamy zrodla lol
                                # usuwamy najpierw wierzcholki, ktore znajduja sie najdalej od zrodla itp.
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1
                res.append(v)

    res = res[::-1]
    print("deleting order (from first to be deleted to last):", res)
    return res

G = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [9, 10], [8], [8]]
pause(G)