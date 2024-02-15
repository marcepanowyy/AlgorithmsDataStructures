# Mamy dane n punkotw (x,y) w okregu o promieniu k (liczba naturalna), tzn.
# 0 <= x^2 + y^2 <= k, które są w nim równomiernie rozłożone tzn. prawdopodobienstwo
# znalezienia punktu na danym obszarze jest proporcjonalne do tego obszaru
# Napisz algorytm, ktory w czasie O(n) posortuje punkty po ich odl. do punktu (0,0)
# tzn. d=sqrt(x^2+y^2)

# bucketsort

# pierwszy bucket to kolo, reszta to pierscienie

# chcemy zeby kazdy bucket (pierscien) mial takie samo pole
# cale pole PI * R^2
# nty pierscien ma pole PI*R^2 /n


# Pi(ri^2 - r(i-1) ^2) = PI R^2 / n

# r
# ri = sqrt(R^2/n + r(i-1)^2)
# dzielimy punkty w zaleznosci od tego

# sortujemy kubelkowo