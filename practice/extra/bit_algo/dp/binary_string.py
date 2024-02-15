# Dostajemy liczbe naturalna n. Naszym zadaniem jest policzenie wszystkich binarnych
# (0/1) stringow o dlugosci n bez jedynek obok siebie

# f(1) = 2  (0, 1)
# f(2) = 3  (00, 01, 10)

# ______01    - ciąg dlugosci n (zostalo n-2)
#_______0     - ciag dlugsci n (zostalo n-1)

# f(i) = f(i-1) + f(i-2)

