# lecture pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja to pewien napis
# składający się z symboli G, A, T i C. Przed dalszymi badaniami konieczne jest upewnić się, że wszystkie
# sekwencje DNA są parami rózne. Proszę opisać algorytm, który sprawdza czy tak faktycznie jest.

# nie moje rozw, ale przyjemne dla oka


class Node:
    def __init__(self):
        self.G = None
        self.A = None
        self.T = None
        self.C = None
        self.end = False


def check_DNA(root, sequence, idx):
    if idx == len(sequence):
        if root.end:
            return False
        root.end = True
        return True
    if sequence[idx] == 'G':
        if root.G is None:
            root.G = Node()
        return check_DNA(root.G, sequence, idx + 1)
    elif sequence[idx] == 'A':
        if root.A is None:
            root.A = Node()
        return check_DNA(root.A, sequence, idx + 1)
    elif sequence[idx] == 'T':
        if root.T is None:
            root.T = Node()
        return check_DNA(root.T, sequence, idx + 1)
    else:
        if root.C is None:
            root.C = Node()
        return check_DNA(root.C, sequence, idx + 1)


def different_sequences_tree(sequence):
    root = Node()
    for i in range(len(sequence)):
        if not check_DNA(root, sequence[i], 0):
            return False
    return True


# mozna tez zrobic drugim sposobem
# literki to cyferki (a sekwencja to liczba), sortuje sie radixem np. TTAG to 1123
# i porownuje sie czy nie ma dwoch takich samych