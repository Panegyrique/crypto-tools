from compute.basic_compute import BASIC_COMPUTE
import math

class ECC():
    
    def __init__(self, a, b, GF):
        # curve => y^2 = x^3 + a*x + b
        self._a = a
        self._b = b
        self._GF = GF
        self._point = []

        self._compute = BASIC_COMPUTE()

    def compute_points(self):
        print(f"\nCalcul des points de la courbe E : y^2 = x^3 + {self._a}*x + {self._b} sur le corps fini GF({self._GF}):")
        print(f"\n\tNous devons tester {self._GF * self._GF} combinaisons de points (x, y):")

        for x in range(self._GF):
            for y in range(self._GF):
                print(f"\t\tVérification : ({x},{y}) sur E ? {y}^2 = {x}^3 + {self._a}*{x} + {self._b} (mod {self._GF})")
                if ((y ** 2) % self._GF) == ((x ** 3 + self._a * x + self._b) % self._GF):
                    print("\t\t=> Vrai, ce point appartient à la courbe")
                    self._point.append((x, y))
                else:
                    print("\t\t=> Faux, ce point n'appartient pas à la courbe")
        
        print(f"\n\t=> Il y a {len(self._point) + 1} points sur la courbe (en comptant le point à l'infini)")
        print(f"\t=> Points trouvés : {sorted(self._point)}\n")

    def add_two_point(self, P, Q):
        print(f"\nAddition de deux points P({P[0]}, {P[1]}) et Q({Q[0]}, {Q[1]}):")
        if P == Q:
            print("\t=> Les points sont égaux, doublement requis")
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

        print("\n\tP + Q = (xr, yr)")
        print("\t\t# xr = [λ^2 - xP - xQ] mod GF")
        print("\t\t# yr = [λ * (xP - xr) - yp] mod GF")
        print("\t\t# λ =  [(yQ - yP) / (xQ - xP)] mod GF")
        self._lambda = ((Q[1] - P[1]) * pow(Q[0] - P[0], -1, self._GF)) % self._GF
        print(f"\n\t=> λ = [({Q[1]} - {P[1]}) / ({Q[0]} - {P[0]})] mod {self._GF} = {self._lambda}")

        x_r = (self._lambda ** 2 - P[0] - Q[0]) % self._GF
        print(f"\t=> xr = [({self._lambda}^2 - {P[0]} - {Q[0]})] mod {self._GF} = {x_r}")
        y_r = (self._lambda * (P[0] - x_r) - P[1]) % self._GF
        print(f"\t=> yr = [{self._lambda} * ({P[0]} - {x_r}) - {P[1]}] mod {self._GF} = {y_r}")
        print(f"\n=> P + Q = ({x_r}, {y_r})")

        return (x_r, y_r)

    def doubling_point(self, P):
        print(f"\nDoublement du point P({P[0]}, {P[1]}):")
        if P == (None, None):
            print("\t=> Le point à l'infini reste le point à l'infini")
            return (None, None)

        if P[1] == 0:
            print("\t=> y = 0, le doublement donne le point à l'infini")
            return (None, None)

        print("\n\t2 * P = (xr, yr)")
        print("\t\t# xr = [λ^2 - 2 * xP] mod GF")
        print("\t\t# yr = [λ * (xP - xr) - yp] mod GF")
        print("\t\t# λ =  [(3 * xP^2 + a) / (2 * yP)] mod GF")
        self._lambda = ((3 * P[0] ** 2 + self._a) * pow(2 * P[1], -1, self._GF)) % self._GF
        print(f"\n\t=> λ = [(3 * {P[0]}^2 + {self._a}) / (2 * {P[1]})] mod {self._GF} = {self._lambda}")

        x_r = (self._lambda ** 2 - 2 * P[0]) % self._GF
        print(f"\t=> xr = [{self._lambda}^2 - 2 * {P[0]}] mod {self._GF} = {x_r}")
        y_r = (self._lambda * (P[0] - x_r) - P[1]) % self._GF
        print(f"\t=> yr = [{self._lambda} * ({P[0]} - {x_r}) - {P[1]}] mod {self._GF} = {y_r}")
        print(f"\n=> 2 * P = ({x_r}, {y_r})")

        return (x_r, y_r)

    def multiply_point(self, k, P):
        R = (None, None)
        for bit in bin(k)[2:]:
            R = self.add_two_point(R, R)
            if bit == '1':
                R = self.add_two_point(R, P)
        return R

    def hasse_weil_borne(self):
        print("\nBorne de Hasse-Weil : [GF + 1 - 2 * sqrt(GF), GF + 1 + 2 * sqrt(GF)]")
        sqrt_GF = math.sqrt(self._GF)
        borne_inferieure = self._GF + 1 - 2 * int(sqrt_GF)
        borne_superieure = self._GF + 1 + 2 * int(sqrt_GF)
        print(f"\t=> [{self._GF} + 1 - 2 * sqrt({self._GF}), {self._GF} + 1 + 2 * sqrt({self._GF})]")
        print(f"\t=> [{borne_inferieure}, {borne_superieure}]")

    def try_generator_p(self, P):
        print(f"\nTest du point {P} comme générateur potentiel:")
        if(len(self._point) == 0):
            print("\t=> Générer tout les points avant de vérifier")
            return
        current_point = P
        generated_points = [P]
        n = 1

        while current_point != (None, None):
            print(f"\n{n}: {current_point}", end='')
            current_point = self.add_two_point(current_point, P)

            if current_point in generated_points:
                print(f"Point {current_point} déjà généré, boucle détectée. Fin du test.")
                break
            if current_point not in self._point and current_point != (None, None):
                print(f"Point {current_point} n'est pas valide sur la courbe. Fin du test.")
                break

            generated_points.append(current_point)
            n += 1

        if len(generated_points) == len(self._point) + 1:  # + 1 pour le point à l'infini
            print(f"\n{P} est un générateur de l'ensemble complet de {n} points (en comptant le point à l'infini).")
        else:
            print(f"\n{P} n'est pas un générateur complet. Il génère seulement {len(generated_points)} points (en comptant le point à l'infini).\n")
            return False
        
        print(f"Points de la courbe : {sorted(self._point)}")
        print(f"Points générés :      {sorted(generated_points[:-1])}")
        return True

    def compute_Kpu(self, Kpr):
        print("\nCalcul de la clé publique Kpu à partir de la clé privée Kpr avec double-and-add:")
        
        if len(self._point) == 0:
            print("\t=> Générer tous les points avant de vérifier")
            return None

        print(f"Clé privée Kpr: {Kpr}")
        P = self._point[0]  
        Kpu = self.multiply_point(Kpr, P)

        if Kpu is None:
            print("\t=> Erreur : Kpu est le point à l'infini, vérifiez Kpr.")
            return None

        print(f"\n=> La clé publique Kpu est {Kpu}.\n")
        return Kpu

    def sign(self, hash_m, k, Kpr):
        print("\nSignature du message avec la méthode ECDSA :")

        if len(self._point) == 0:
            print("\t=> Générer tous les points avant de vérifier")
            return None, None
        
        r = len(self._point) + 1

        print(f"Hash du message: {hash_m}")
        print(f"r: {r}")
        print(f"k: {k} (doit être dans [1, r-1] et pgcd(k, r) = 1)")
        if self._compute.pgcd(k, r)[0] != 1:
            print("\t=> Erreur : pgcd(k, r) != 1, générer un nouveau k.")
            return None, None
        
        print("\nÉtape 1: R = k * P")
        R = self.multiply_point(k, self._point[0])
        print(f"=> x_k = {R[0]}")

        if R is None: 
            print("\t=> Erreur : kP a donné le point à l'infini, générer un nouveau k.")
            return None, None

        print("\nÉtape 2 : sigma_1 = x_R mod r")
        x_R = R[0]
        sigma_1 = x_R % r
        print(f"=> sigma_1 = {x_R} mod {r} = {sigma_1}")

        if sigma_1 == 0:
            print("\t=> Erreur : r est 0, générer un nouveau k.")
            return None, None

        print("\nÉtape 3 : sigma_2 = k^(-1) * (H(M) + sigma_1 * Kpr) mod r")
        k_inv = self._compute.euclide_extended(k, r)
        sigma_2 = (k_inv * (hash_m + sigma_1 * Kpr)) % r
        print(f"=> sigma_2 = {k_inv} * ({hash_m} + {sigma_1} * {Kpr}) mod {r}")

        if sigma_2 == 0:
            print("\t=> Erreur : s est 0, générer un nouveau k.")
            return None, None

        print(f"\n=> La signature est (sigma_1, sigma_2) = ({sigma_1}, {sigma_2}).")
        return sigma_1, sigma_2

    def verif_sign(self, hash_m, sigma_1, sigma_2, Kpu):
        print("\nVérification de la signature avec la méthode ECDSA :")

        if len(self._point) == 0:
            print("\t=> Générer tous les points avant de vérifier")
            return None, None
        
        r = len(self._point) + 1

        print("\nÉtape 1: vérifier 1 <= sigma_1 <= r - 1 et 1 <= sigma_2 <= r - 1")
        if not (1 <= sigma_1 <= r - 1):
            print("\t=> Erreur : sigma_1 n'est pas dans [1, r-1]")
            return False
        if not (1 <= sigma_2 <= r - 1):
            print("\t=> Erreur : sigma_2 n'est pas dans [1, r-1]")
            return False
        print("=> Vrai")

        print("\nV = (H(M) * sigma_2^-1) * P + (sigma_1 * sigma_2^-1) * Kpu")

        print("\nÉtape 2: R1 = (H(M) * sigma_2^-1) * P")
        sigma_2_inv = self._compute.euclide_extended(sigma_2, r)
        H_M = hash_m % r #
        R1 = self.multiply_point(H_M * sigma_2_inv, self._point[0])

        print("\nÉtape 3: R2 = (sigma_1 * sigma_2^-1) * Kpu")
        fac = (sigma_1 * sigma_2_inv) % r #
        R2 = self.multiply_point(fac, Kpu)
        
        print("\nÉtape 4: V = R1 + R2")
        V = self.add_two_point(R1, R2)
        print(f"=> V = {V}")

        print("\nÉtape 5: xV == sigma_1 mod r ?")
        xV_result = V[0] % r 
        print(f"=> xV calculé: {xV_result}, attendu: {sigma_1}")
        
        if xV_result == sigma_1:
            print("\t=> La signature est valide.")
            return True
        else:
            print("\t=> La signature est invalide.")
            return False
    