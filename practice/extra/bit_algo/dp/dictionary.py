# Dana jest zawsze dzialajaca w czasie O(1) funkcja dict(word), ktora mowi
# czy slowo word jest poprawnym slowem danego jezyka. Dostajemy na wejsciu
# stringa bez spacji. Podaj algorytm, ktory stwierdzi, czy da sie tak powstawiac
# spacje do wejsciowego stringa, ze ciag slow, ktory otrzymamy tworza slowa
# z danego jezyka. Np. "alamakotainiemapsa" mozemy zapisac jako
# "ala ma kota i nie ma psa". Podaj rowniez, jak wykorzystac algorytm
# aby uzyskac przykladowe poprawne rozdzielenie stringa spacjami, jesli
# oczywiscie ono istnieje.

# f(i) - czy do itego indeksu mozna podzielic tekst na slowa w slowniku
# f(i) = f(k) and dict(txt[k+1:i]) dla k<i

def get_parent(dict, word):
    n = len(dict)
    for i in range(n):
        if dict[i] == word: return i
    return -1

def dictionary(txt, dict):

    n = len(txt)
    can_divide = [False] * n
    parents = [None] * n

    for i in range(n):
        for k in range(i):
            if txt[k:i+1] in dict and (can_divide[k-1] == True if k != 0 else 1):
                can_divide[i] = True
                parents[i] = get_parent(dict, txt[k:i+1])

    def get_solution(parents, dict, index):
        if index < 0: return []
        return [dict[parents[index]]] + get_solution(parents, dict, index - len(dict[parents[index]]))

    if can_divide[n-1]:
        res = get_solution(parents, dict, n-1)[::-1]
        print("words to create the input txt:", res)
    else:
        print("we couldnt create the input txt out of the words in dictionary")


dict1 = ["amkaras", "kar", "am", "as", "akar"]
txt1 = "asamkarasb"
# dictionary(txt1, dict1)

dict2 = ["kot", "ma", "ale", "ala", "jest", "hoe"]
txt2 = "alaalemahoemaale"
# dictionary(txt2, dict2)

# essa