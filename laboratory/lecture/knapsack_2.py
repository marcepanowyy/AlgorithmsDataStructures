# Dane:

# I = {0, 1, ..., n-1} - przedmioty
# w: I -> N - wagi
# p: I -> N - ceny/profity
# B - max waga

# zadanie: znalezc podbzior I o maksymalnej sumarycznej cenie
# i lacznej wadze nie przekraczajacej B

# 1. Funkcja do obliczania
# f(i, b) = maksymalna suma cen przedmiotow ze zbioru {0, ..., i}
# nie przekraczajacych lacznej wagi b

# wynik: f(n-1, B)

# 2. Sformułowanie rekurencyjne
# f(i, b) = max(f(i-1, b), f(i-1, b-w(i)) + p(i)) jesli b-w(i) >= 0
#                 bierzemy albo nie bierzemy es

# f(0, b) = p(0) if w(0) <= b else 0


















