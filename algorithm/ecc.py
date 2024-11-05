import math

class ECC():
    
    def __init__(self, a, b, GF):
        # curve => y^2 = x^3 + a*x + b
        self._a = a
        self._b = b
        self._GF = GF
        self._point = []

    def compute_points(self):
        print(f"\nCalcul des points de la courbe E : y^2 = x^3 + {self._a}*x + {self._b} sur le corps fini GF({self._GF})")
        print(f"Nous devons tester {self._GF * self._GF} combinaisons de points (x, y)")

        for x in range(self._GF):
            for y in range(self._GF):
                print(f"Vérification : ({x},{y}) sur E ? {y}^2 = {x}^3 + {self._a}*{x} + {self._b} (mod {self._GF})")
                if ((y ** 2) % self._GF) == ((x ** 3 + self._a * x + self._b) % self._GF):
                    print("\t=> Vrai, ce point appartient à la courbe")
                    self._point.append((x, y))
                else:
                    print("\t=> Faux, ce point n'appartient pas à la courbe")
        
        print(f"\nIl y a {len(self._point) + 1} points sur la courbe (en comptant le point à l'infini)")
        print(f"Points trouvés : {self._point}\n")

    def add_two_point(self, P, Q):
        print("\nAddition de deux points P et Q :")
        if P == Q:
            print("\t=> Les points sont égaux, doublement requis", end='')
            return self.doubling_point(P)

        if P == (None, None):
            print("\t=> P est le point à l'infini, résultat = Q")
            return Q
        if Q == (None, None):
            print("\t=> Q est le point à l'infini, résultat = P")
            return P

        if (Q[0] - P[0]) % self._GF == 0:
            print("\t=> Les points sont alignés verticalement, résultat = point à l'infini")
            return (None, None)

        # Calcul de la pente (lambda)
        self._lambda = ((Q[1] - P[1]) * pow(Q[0] - P[0], -1, self._GF)) % self._GF
        print(f"\tλ (lambda) = ({Q[1]} - {P[1]}) * (inverse de {Q[0]} - {P[0]}) mod {self._GF} = {self._lambda}")

        print(f"\txr = (λ^2 - Px - Qx) mod GF")
        x_r = (self._lambda ** 2 - P[0] - Q[0]) % self._GF
        print(f"\tyr = (λ * (Px - xr) - Py) mod GF")
        y_r = (self._lambda * (P[0] - x_r) - P[1]) % self._GF
        print(f"\t=> Point résultant : ({x_r}, {y_r})\n")

        return (x_r, y_r)

    def doubling_point(self, P):
        print("\nDoublement du point P :")
        if P == (None, None):
            print("\t=> Le point à l'infini reste le point à l'infini")
            return (None, None)

        if P[1] == 0:
            print("\t=> y = 0, le doublement donne le point à l'infini")
            return (None, None)

        # Calcul de la pente (lambda)
        self._lambda = ((3 * P[0] ** 2 + self._a) * pow(2 * P[1], -1, self._GF)) % self._GF
        print(f"\t=> λ (lambda) = (3 * {P[0]}^2 + {self._a}) * (inverse de 2 * {P[1]}) mod {self._GF} = {self._lambda}")

        x_r = (self._lambda ** 2 - 2 * P[0]) % self._GF
        y_r = (self._lambda * (P[0] - x_r) - P[1]) % self._GF
        print(f"\t=> Point résultant : ({x_r}, {y_r})\n")

        return (x_r, y_r)

    def hasse_weil_borne(self):
        sqrt_GF = math.sqrt(self._GF)
        borne_inferieure = self._GF + 1 - 2 * int(sqrt_GF)
        borne_superieure = self._GF + 1 + 2 * int(sqrt_GF)
        print(f"\nBorne de Hasse-Weil : [{borne_inferieure}, {borne_superieure}]")
        print(f"Calculée comme [{self._GF} + 1 - 2*sqrt({self._GF}), {self._GF} + 1 + 2*sqrt({self._GF})]\n")

    def try_generator_p(self, P):
        print(f"\nTest du point {P} comme générateur potentiel :")
        current_point = P
        generated_points = [P]
        n = 1

        while current_point != (None, None):
            print(f"{n}: {current_point}", end='')
            current_point = self.add_two_point(current_point, P)

            if current_point in generated_points:
                print(f"Point {current_point} déjà généré, boucle détectée. Fin du test.")
                break
            if current_point not in self._point and current_point != (None, None):
                print(f"Point {current_point} n'est pas valide sur la courbe. Fin du test.")
                break

            generated_points.append(current_point)
            n += 1

        if len(generated_points) == len(self._point) + 1:  # +1 pour le point à l'infini
            print(f"\n{P} est un générateur de l'ensemble complet de {n} points.")
        else:
            print(f"\n{P} n'est pas un générateur complet. Il génère seulement {len(generated_points)} points.\n")
