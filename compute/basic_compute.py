from sympy import isprime
import math

class BASIC_COMPUTE:

    def __init__(self):
        pass

    def _is_perfect_square(self, x):
        s = int(math.sqrt(x))
        result = s * s == x
        return result
    
    def pgcd(self, a, b):
        print(f"\nPGCD({a}, {b}):")
        steps = []
        while b != 0:
            quotient = a // b
            reste = a % b
            steps.append((a, b, quotient, reste))
            print(f"\t{a} = {quotient} * {b} + {reste}")
            a, b = b, reste
        print(f"\n\t=> PGCD = {a}")
        return a, steps

    def euclide_extended(self, a, n):
        print(f"\nEuclide étendu: a * {a} = 1 mod {n}")
        _, steps = self.pgcd(a,n)
        steps.pop(-1)

        x0, x1 = 1, 0
        y0, y1 = 0, 1

        print("\nRemontée avec Euclide étendu:")
        for i, (a, n, quotient, reste) in enumerate(reversed(steps)):
            if i == 0:
                print(f"\tOn part de 1 = {a} - {quotient} * {n}")
            x0, x1 = x1, x0 - quotient * x1
            y0, y1 = y1, y0 - quotient * y1

        print(f"\t1 = {y0} * {a} + {x0} * {n}")

        inverse = y0 % n
        if inverse < 0:
            inverse += n
        
        print(f"\n=> 1 = {y0} * {a} + {x0} * {n} (mod {n}) donc a = {inverse}")
        return inverse
    
    def modular_exponentiation(self, a, b, n, display=True):
        if display:
            print(f"\nModular Exponentiation: {a} ^ {b} mod {n}")
        result = 1
        a = a % n

        for i in range(1, b + 1):
            if display:
                print(f"\t{i}: ({result} * {a}) % {n} = ", end='')
            result = (result * a) % n
            if display:
                print(result)

        if display:
            print(f"\n\t=> {a} ^ {b} mod {n} = {result}")
        return result

    def square_and_multiply(self, a, b, n, display=True):
        if display:
            print(f"\nSquare and Multiply: {a} ^ {b} mod {n}")
        result = 1
        a = a % n

        binary_b = bin(b)[2:]
        if display:
            print(f"\tbin({b}) = {binary_b}")

        for i, bit in enumerate(binary_b):
            if display:
                print(f"\t{i}: Square: ({result} * {result}) % {n} = ", end='')
            result = (result * result) % n
            if display:
                print(result)
            
            if bit == '1':
                if display:
                    print(f"\t   Multiply: ({result} * {a}) % {n} = ", end='')
                result = (result * a) % n
                if display:
                    print(result)
            else:
                if display:
                    print("\t   Pas de multiplication bit = 0")

        if display:
            print(f"\n\t=> {a} ^ {b} mod {n} = {result}")
        return result
    
    def modular_square_root(self, a, n):
        print(f"\nRacine carré modulaire: {a} mod {n}")
        roots = []

        for x in range(n):
            print(f"\t{x}: ({x} * {x}) % {n} = ", end='')
            if (x * x) % n == a:
                print(f"{a} => Vrai")
                roots.append(x)
            else:
                print(f"{(x * x) % n} => Faux")

        if roots:
            print(f"\n\t=> Racines carrées mod {n} de {a} = {roots}")
        else:
            print(f"\n\t=> Pas de racines carrées mod {n} trouvées pour {a}")

        return roots
    
    def primality_test(self, a):
        print(f"\n{a} est un nombre premier ?")
        
        if isprime(a):
            print(f"\t=> {a} est un nombre premier.")
            return True
        else:
            print(f"\t=> {a} n'est pas un nombre premier.")
            return False
    
    def is_generator(self, group_order, g):
        print(f"\n{g} est un générateur de l'ensemble multiplicatif modulo {group_order + 1} ?")
        print(f"Le groupe a un ordre de {group_order}. Nous devons vérifier si les puissances de {g} couvrent tous les entiers de 1 à {group_order} modulo {group_order + 1}")
        
        seen = set() # Build a set of unique elements
        for k in range(1, group_order + 1):
            power = self.square_and_multiply(g, k, group_order + 1, display=False)
            seen.add(power)
            print(f"\t{k}: {g}^{k} mod {group_order + 1} = {power}")
        
        if len(seen) == group_order:
            print(f"\n\t=> {g} est un générateur car toutes les valeurs de 1 à {group_order} sont atteintes.")
            return True
        else:
            print(f"\n\t=> {g} n'est pas un générateur car toutes les valeurs de 1 à {group_order} ne sont pas atteintes.")
            return False
    
    def fermat_factorization(self, n):
        print(f"\nFactorisation de {n} par la méthode de Fermat:")
        
        if n % 2 == 0:
            print(f"\t{n} est pair, donc on a immédiatement une factorisation : 2 * {n // 2}")
            return (2, n // 2)

        a = math.ceil(math.sqrt(n))
        print(f"\tOn commence avec a = ⌈√{n}⌉ = {a}")

        b2 = a * a - n
        print(f"\tInitialement, b² = {a}² - {n} = {b2}")

        step = 0
        while not self._is_perfect_square(b2):
            print(f"\n\t{step}: b² = {b2} n'est pas un carré parfait.")
            a += 1
            print(f"\t   On incrémente a pour obtenir a = {a}")
            b2 = a * a - n
            print(f"\t   On recalcule b² : {a}² - {n} = {a * a} - {n} = {b2}")
            step += 1

        # Une fois b² trouvé comme un carré parfait
        b = int(math.sqrt(b2))
        print(f"\n\tTrouvé !!! b² = {b2} qui est un carré parfait, donc b = √{b2} = {b}")

        # Calcul des facteurs p et q
        p = a - b
        q = a + b
        print(f"\t\t   On calcule les facteurs :")
        print(f"\t\t   p = a - b = {a} - {b} = {p}")
        print(f"\t\t   q = a + b = {a} + {b} = {q}")
        print(f"\t\t   Vérification : p * q = {p} * {q} = {p * q}")

        print(f"\n\t=> Les facteurs de {n} sont {p} et {q} (car {p} * {q} = {n})")
        return (p, q)

    def discrete_logarithm(self, a, b, n, card):
        print(f"\nCalcul du logarithme discret de {b} en base {a} modulo {n} :")
        
        m = math.ceil(math.sqrt(card)) # Approximativement √n
        print(f"\nÉtape 1: \n\tm = ⌊√{card}⌋ = {m}")

        print('\nÉtape 2: Calculer les étapes "baby" : a^j mod n')
        baby_steps = {}
        for j in range(m):
            value = self.modular_exponentiation(a, j, n, display=False)
            baby_steps[value] = j
            print(f"\tBaby step: a^{j} mod {n} = {value}")
        
        print("\t=>", sorted(baby_steps.items()))

        print("\nÉtape 3 : Calculer a^(-m) mod n")
        a_inv_m = self.euclide_extended(a, n)  # Calculer l'inverse de a mod n
        a_inv_m = self.modular_exponentiation(a_inv_m, m, n)
        print(f"\t=> a^(-m) mod {n} = {a_inv_m}")

        print('\nÉtape 4 : Calculer les étapes "giant"')
        giant_step_value = b
        for i in range(m):
            print(f"\t{i}: Giant step = {giant_step_value}")
            
            if giant_step_value in baby_steps:
                print(f"\t   On a trouvé {giant_step_value} à l'étape {i} !")
                print(f"\n\t=> Logarithme discret : x = {i} * {m} + {baby_steps[giant_step_value]} = {i * m + baby_steps[giant_step_value]}")
                return i * m + baby_steps[giant_step_value]
            
            print(f"\t   {giant_step_value} n'est pas trouvé dans les baby steps. On passe à l'étape suivante.")
            temp = giant_step_value
            giant_step_value = (giant_step_value * a_inv_m) % n
            print(f"\t   On calcule le nouveau giant_step_value = ({temp} * {a_inv_m}) % {n} = {giant_step_value}")

        print("\t=> Logarithme discret non trouvé.")
        return None

    def list_of_squares(self, x):
        print(f"\nListe des carrés dans le corps F_{x}:")
        squares = []

        for i in range(x):
            square = (i * i) % x
            squares.append(square)
            print(f"\t{i}^2 mod {x} = {square}")
        
        unique_squares = sorted(set(squares))
        print(f"\n\t=> Carrés distincts dans F_{x} = {unique_squares}")
        
        return unique_squares
    