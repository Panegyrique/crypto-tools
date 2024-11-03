from sympy import isprime

class BASIC_COMPUTE:

    def __init__(self):
        pass
    
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
        