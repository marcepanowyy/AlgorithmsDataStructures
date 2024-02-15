# Sklejanie odcinkow

# Dany jest ciag przedzialow postaci [ai, bi]. Dwa przedzialy mozna skleic,
# jesli maja dokladnie jeden punkt wspolny. Prosze wskazac algorytmy dla
# nastepujacych problemow

# 1. Problem stwierdzenia, czy da sie uzyskac przedzial [a, b] przez sklejanie odcinkow - DIJKSTRA
# 2. Zadanie jak wyzej, ale kazdy odcinek ma koszt i pytamy o minimalny koszt
# uzyskania odcinka [a, b] - DIJKSTRA
# 3. Problem stwierdzenia jaki najdluzszy odcinek mozna uzyskac sklejajac najwyzej k odcinkow
# - LONGEST PATH

# tworzymy graf (lista sasiedztwa) n**2
# [1, 2], [2, 8] - wierzcholek 1 polaczony z wierzcholkiem 2
# i wierzcholek 2 polaczony z wierzcholkiem 8
# nastepnie alg. Dijkstry es

