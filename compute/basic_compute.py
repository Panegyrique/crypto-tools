class BASIC_COMPUTE:

    def __init__(self):
        pass
    
    def pgcd(self, a, b):
        print(f"\nPGCD({a}, {b}) :")
        steps = []
        while b != 0:
            quotient = a // b
            reste = a % b
            steps.append((a, b, quotient, reste))
            print(f"\t{a} = {quotient} * {b} + {reste}")
            a, b = b, reste
        print(f"\n\t=> PGCD = {a}")
        return a, steps

    def euclide_extended(self, a, b):
        print(f"\nEuclide étendu : a * {a} = 1 mod {b}")
        _, steps = self.pgcd(a,b)
        steps.pop(-1)

        x0, x1 = 1, 0
        y0, y1 = 0, 1

        print("\nRemontée avec Euclide étendu :")
        for i, (a, b, quotient, reste) in enumerate(reversed(steps)):
            if i == 0:
                print(f"\tOn part de 1 = {a} - {quotient} * {b}")
            x0, x1 = x1, x0 - quotient * x1
            y0, y1 = y1, y0 - quotient * y1

        print(f"\t1 = {y0} * {a} + {x0} * {b}")

        inverse = y0 % b
        if inverse < 0:
            inverse += b
        
        print(f"\n=> 1 = {y0} * {a} + {x0} * {b} (mod {b}) donc a = {inverse}")
        return inverse
    
    def modular_exponentiation(self, a, b, n):
        print(f"\nModular Exponentiation : {a} ^ {b} mod {n}")
        result = 1
        a = a % n

        for i in range(1, b + 1):
            print(f"\t{i}: ({result} * {a}) % {n} = ", end='')
            result = (result * a) % n
            print(result)

        print(f"\n\t=> {a} ^ {b} mod {n} = {result}")
        return result

    def square_and_multiply(self, a, b, n):
        print(f"\nSquare and Multiply : {a} ^ {b} mod {n}")
        result = 1
        a = a % n

        binary_b = bin(b)[2:]
        print(f"\tbin({b}) = {binary_b}")

        for i, bit in enumerate(binary_b):
            print(f"\t{i}: Square: ({result} * {result}) % {n} = ", end='')
            result = (result * result) % n
            print(result)
            
            if bit == '1':
                print(f"\t   Multiply: ({result} * {a}) % {n} = ", end='')
                result = (result * a) % n
                print(result)
            else:
                print("\tPas de multiplication bit = 0")

        print(f"\n\t=> {a} ^ {b} mod {n} = {result}")
        return result
    
    def primality_test():
        pass