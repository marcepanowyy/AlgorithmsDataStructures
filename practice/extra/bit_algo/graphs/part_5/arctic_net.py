# Akrtyczna siec

# lecture Akrtyce osady sa oddalone od siebie na ogromne odleglosci. Otrzymujemy je jako pary
# wspolrzednych (x, y). Niektore z nich posiadaja odbiorniki satelitarne - z takiej osady
# mozna bezposrednio komunikowac sie z kazda inna osada, ktora ma odbiornik satelitarny.

# Chcemy teraz w kazdej osadzie umiejscowic radioodbiorniki o tym samym ograniczonym
# zasiegu D (liczba calkowita), aby mozna bylo sie komunukowac (posrednio lub bezposrednio)
# miedzy kazda para osad. Jakie jest minimalne D, ktore pozwoli osiagnac ten cel?

# Uzasadnij poprawnosc rozwiazania.

# tworzymy graf pelny
# szukamy mst (ale najpierw union miedzy miastami z odbiornikami satelitarnymi)
# waga ostantniej dolozonej krawedzi jest rozwiazaniem