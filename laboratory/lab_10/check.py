# (Szachuję)
# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto
# jest otoczone murem i ma tylko dwie bramy - północną i południową. Z każdej bramy prowadzi dokładnie
# jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być
# połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
# zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
# miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze
# stolicy Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić
# algorytm, który stwierdza czy odpowiednia trasa gońca istnieje.

# Krok 1: Zamiana miast na krawędzie
# (Jeżeli jest kilka kolejno połączonych ze sobą miast, trakrujemy je jako jedną krawędź, ponieważ,
# gdy wejdziemy do pierwszego spośród tych miast, musimy przejść przez wszystkie kolejne)

# Krok 2: Scalanie oaz, które są połączone krawędziami, przez które możemy przejść wiele razy

# scalanie -> euler