# [2pkt.] Zadanie 2.
# Szablon rozwiązania: zad2.py

# Dana jest tablica haszująca o rozmiarze N elementów oparta o adresowanie otwarte i liniowe rozwiązywanie konfliktów (z krokiem 1; dokładny kod wstawiania do tablicy znajduje się w funkcji
# insert w pliku zad2 te.st .. y.py). Każdy element tablicy jest obiektem zawierającym klucz (napis)
# oraz pole wskazujące, czy element jest zajęty:
# class Node:
# def __init__(self, key = None, taken = False):
# self.key = key
# self.taken = taken
# Ponadto dana jest funkcja haszująca h(key) przyjmująca klucz i zwracająca indeks w tablicy (w
# przedziale 0 do N-1; w pliku zad2.py wpisana jest konkretna wartość N, ale w ogólności nie należy
# traktować N jako stałej).
# Niestety, w wyniku ataku komputerowego dokładnie jeden elementy tablicy haszującej zostały zmodyfikowany poprzez zmianę wartości pola taken na False oraz pola Klucz na None. Proszę zaproponować i zaimplementować funkcję:
# def recover(hash_tab):
# ...
# która sprawdza, czy w tablicy haszującej przekazanej przez argument wszystkie elementy z polem
# taken równym True mogą być poprawnie znalezione (procedura wyszukiwania w tablicy haszującej to find z pliku za d2 te s ty. .py). Jeżeli tak nie jest, funkcja powinna „naprawić” tablicę w taki
# sposób, by wszystkie elementy (w których taken == True) były osiągalne. lecture każdym przypadku
# funkcja powinna zwrócić tablicę (potencjalnie naprawioną) jako wynik. Funkcja może używać jedynie stałego (niezależnego od N) rozmiaru dodatkowej pamięci operacyjnej (a więc powinna działać
# w miejscu - nie można dodawać pól do elementów tablicy lub utworzyć nowej tablicy haszującej).
# Zaproponowane rozwiązanie powinno być możliwie jak najszybsze.