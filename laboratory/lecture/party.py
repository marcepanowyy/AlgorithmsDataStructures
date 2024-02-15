# f(v) - wartosc najlepszej imprezy w T(v)
# g(v) - wartosc najlepszej imprezy w T(v), na ktora v nie idzie

# g(v) = Suma po u z f(u) (u - bezposredni pracownik v)
# f(v) = max(g(v), v.fun + suma po u z g(u)) (u - bezposredni pracownik v)

class Employee:
    def __init__(self, fun):
        self.emp = []
        self.f = -1
        self.g = -1
        self.fun = fun

def f(v):
    if v.f >= 0: return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f

def g(v):
    if v.g >= 0: return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g