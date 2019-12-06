from points import Point
import matplotlib.pyplot as plt
import random

def orientation(p, q, r):
    """
    sprawdzanie orientacji 3 punktow
    0 gdy sa wspolliniowe
    1 gdy sa ulozone w kierunku ruchu wskazowek zegara
    2 gdy sa ulozone przeciwnie do ruchu wskazowek zegara
    """
    val = ((q.y-p.y) * (r.x-q.x)) - ((q.x-p.x) * (r.y-q.y))
    if val == 0:
        return 0
    return 1 if (val > 0) else 2


def graham(L):
    """
    Wyznaczanie otoczki wypuklej z podanej listy
    -znalezenie punktu o najmniejszej wsp. y
    -sortowanie listy bez pierwszego elementu wg wspolrzednych polarnych
    -znaleznie punktow nalezacych do otoczki    
    """
    
    if len(L) < 3:
        return L 

    bottom = 0
    for i in range (1, len(L)):
        if L[i].y < L[bottom].y:
            bottom = i
        
    L[0], L[bottom] = L[bottom], L[0]
    pivot = L[0]

    def polar_order(a, b):
        """
        ustalanie polozenia wg wspolrzednych polarnych,
        najpierw kat, potem odleglosc
        """
        order = orientation(pivot, a, b)
        if order == 0:
            return -1 if ((pivot - a).length() < (pivot - b).length()) else 1
        return -1 if (order == 2) else 1


    L[1:] = sorted(L[1:], polar_order)

    stack = []
    stack.append(L[0])
    stack.append(L[1])

    """
    sprawdzanie orientacji danej trojki
    jesli jest wspolniowy lub preciwny do ruchu wskazowek zegara,
    zostawiamy na stosie w przeciwnym wypadku usuwamy ze stosu
    """
    for i in range (2, len(L)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], L[i]) != 2:
            stack.pop()
        stack.append(L[i])

    return stack

def generate_list():
    """
    przygotowanie listy i losowa generacja punktow
    """
    L = []
    for i in range(0, 100):
        x = random.randint(-20, 20)
        y = random.randint(-20, 20)
        L.append(Point(x, y))
    return L

def draw(L, graham_L):
    """
    odzielne zapisanie czesci ze wspolrzedna x i y z obu list,
    oraz rysowanie
    """
    xL = [p.x for p in L]
    yL = [p.y for p in L]
    xG = [p.x for p in graham_L]
    yG = [p.y for p in graham_L]

    plt.plot(xL, yL, 'o')
    for i in range(0, len(xG)):
        if i == len(xG) - 1:
            temp = 0
        else:
            temp = i + 1
        plt.plot([xG[i], xG[temp]], [yG[i], yG[temp]], 'r--')
    
    plt.show()
