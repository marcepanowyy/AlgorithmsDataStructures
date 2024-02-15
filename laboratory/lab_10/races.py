# Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi mają się odbywać po trasach
# zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji. Król chce, żeby każde
# miasto było zaangażowane w dokładnie jeden wyścig. lecture tym celu należy sprawdzić, czy da się wynająć
# odpowiednie odcinki autostrad. Należy jednak pamiętać o następujących ograniczeniach:
#   1) w Bitocji wszystkie autostrady są jednokierunkowe,
#   2) z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
# miast,
#   3) do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
# miast.

# Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
# zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.


# lecture tym przypadku mamy taką sytuację, że do danego miasta mogą dochodzić maksymalnie dwie krawędzie,
# ale tylko jedna z nich może być fragmentem trasy, na której odbywa się wyścig,
# ponieważ dane miasto może uczestniczyć tylko w jednym wyścigu w danym czasie.

# Ponieważ również chcemy sprawdzić, czy możliwe jest, aby wszystkie miasta uczestniczyły w jakimś wyścigu,
# musimy sprawdzić tak naprawdę, czy dla każdego miasta przynajmniej jedna z krawędzi wchodzących (jeżeli są dwie)
# lub dokładnie jedna (jeżeli jest jedna) znajduje się na trasie danego wyścigu. Jeżeli z danego miasta wychodzi
# jedna krawędź, to ta krawędź również musi uczestniczyć w wyściugu, a jeżeli są dwie, to dokładnie jedna z tych
# dwóch musi uczestniczyć w wyścigu.

# Problem da się rozwiązać, przekształacając nasze zagadnienie na formułę w postaci CNF i
# sprawdzając, czy jest ona spełnialna.


# Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych cen i należy wybrać wspólną cenę
# dla wszystkich wynajętych odcinków.
# Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych cen i należy wybrać wspólną cenę

