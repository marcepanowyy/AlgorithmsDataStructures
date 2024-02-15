# Srednica drzewa nazywamy odleglosc miedzy jego najbardziej oddalonymi od siebie
# wierzcholkami. Napisz algorytm, ktory przyjmujac na wejsciu drzewo (niekoniecznie binarne)
# w postaci listy krawedzi zwroci jego srednice

# 2 wywolania dfs
# za pierwszym razem odpalamy z dowolnego wierzcholka u
# znajdujemy dzieki temu wierzcholek najbardziej odlegly od u, wierzcholek t
# z wierzcholka t odpalamy drugi raz dfs znajdujac drugi najbardziej odlegly
# wierzcholek od wierzcholka t, wierzcholek s
# odleglosc miedzy s i t to srednica
