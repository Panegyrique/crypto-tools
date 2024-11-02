import math

class ECC():
    
    def __init__(self, a, b, GF):
        # curve => y^2 = x^3 + a*x + b
        self._a = a
        self._b = b
        self._GF = GF
        self._point = []

    def compute_points(self):
        rational_limit = self._GF * self._GF
        for x in range(self._GF):
            for y in range(self._GF):
                print(f"({x},{y}) dans E ? {y}^2 = {x}^3 + {self._a}*{x} + {self._b} modulo({self._GF})")
                if ((y ** 2)%self._GF) == ((x ** 3 + self._a * x + self._b)%self._GF):
                    print("\t=> Vrai")
                    self._point.append((x,y))
                else:
                    print("\t=> Faux")
        print(f"\nIl y a {len(self._point)+1} point sur la courbe E (en comptant le point à l'infini)\n{self._point}")

    def add_two_point(self, P, Q):
        self._lambda = None
        pass

    def doubling_point(self, p):
        self._lambda = None
        pass

    def hasse_weil_borne(self):
        pass
    