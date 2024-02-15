# Given n boxes [(L1, W1, H1), (L2, W2, H2), ... (Ln, Wn, Hn)] where box i has
# length Li, width Wi and height Hi, find the height of the tallest possible stack.
# Box (Li, Wi, Hi) can be on top of box (Lj, Wj, Hj) if Li < Lj and Wi < Wj

# sortujemy po pierwszej lub po drugiej wspolrzednej
# nastepnie sprawdzamy dla kazdego pudelka czy da sie przedluzyc maksymalna wysokosc


def can_be_stacked(box1, box2):
    if box1[0] < box2[0] and box1[1] < box2[1]:
        return True
    return False

def find_index(i, h): # find index with max value in a particular row
    n = len(h)
    index = -1
    max_value = 0
    for j in range(n):
        if h[i][j] > max_value:
            max_value = h[i][j]
            index = j
    return index

def get_solution(h, bottom_idx, T):
    res = []
    res.append(T[bottom_idx])
    index = find_index(bottom_idx, h)
    while index != -1:
        res.append(T[index])
        index = find_index(index, h)
    return res

def max_height(T):
    n = len(T)
    T.sort(key=lambda x: x[0])
    h = [[0 for _ in range(n)] for _ in range(n)]
    height = 0
    bottom_idx = -1

    for i in range(1, n):
        box1 = T[i]
        for j in range(i):
            box2 = T[j]
            if can_be_stacked(box2, box1):
                h[i][j] = max(max(h[j])+box1[2], box1[2]+box2[2])
                if h[i][j] > height:
                    height = h[i][j]
                    bottom_idx = i


    res = get_solution(h, bottom_idx, T)
    print("maximum height is", height)
    print("boxes used to build that height: ", res)
    return height


T = [(4,5,3), (2,3,2), (3,6,2), (1,5,4), (2,4,1), (1,2,2)]
max_height(T)
