from compute.basic_compute import BASIC_COMPUTE

class ELGAMAL:

    def __init__(self, p, g, h, x=None):
        self._p = p
        self._g = g
        self._h = h
        self._x = x

        self._compute = BASIC_COMPUTE()
        
    def encrypt(self, m, k):
        # c = g^k mod p et c2 = m * h^k mod p
        c1 = self._compute.modular_exponentiation(self._g, k, self._p)
        a = self._compute.modular_exponentiation(self._h, k, self._p)
        c2 = (m * a) % self._p
        print(f"\nChiffrement : c1 = {self._g}^{k} mod {self._p}\n\t\t= {c1}")
        print(f"Chiffrement : c2 = {m} * {self._h}^{k} mod {self._p}\n\t\t= {c2}")
        return c1, c2

    def decrypt(self, c1, c2):
        s = self._compute.modular_exponentiation(c1, self._x, self._p)
        s_inv = self._compute.euclide_extended(s, self._p)
        decrypted_message = (c2 * s_inv) % self._p
        print(f"Déchiffrement de ({c1},{c2}): m = {c2} * {s_inv} mod {self._p}\n\t\t= {decrypted_message}")
        return decrypted_message

    def verify_private_key(self, x):
        if pow(self._g, x, self._p) == self._h:
            print(f"\n{x} est la clé privée car {self._g}^{x} mod {self._p} = {self._h}")
            self._x = x
            return True
        else:
            print(f"\n{x} n'est pas la clé privée car {self._g}^{x} mod {self._p} ≠ {self._h}")
            return False

    def brute_force_private_key(self):
        for x in range(1, self._p):  # x varie de 1 à p-1
            if pow(self._g, x, self._p) == self._h:
                self._x = x
                print(f"\nClé privée retrouvée par brute force : x = {x}")
                return
        print("\nAucune clé privée n'a été trouvée")
