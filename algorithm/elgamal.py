class ELGAMAL:

    def __init__(self, p, g, h, x=None):
        self._p = p
        self._g = g
        self._h = h
        self._x = x
        

    def encrypt(self, m, k):
        # c = g^k mod p et c2 = m * h^k mod p
        c1 = pow(self._g, k, self._p)
        c2 = (m * pow(self._h, k, self._p)) % self._p
        print(f"Chiffrement : c1 = {self._g}^{k} mod {self._p}\n\t\t= {c1}")
        print(f"Chiffrement : c2 = {m} * {self._h}^{k} mod {self._p}\n\t\t= {c2}")
        return c1, c2


    def decrypt(self, c1, c2):
        if self._x is None:
            print("Erreur : La clé privée x n'est pas définie")
            return
        
        # s = c1^x mod p et m = c2 * s^(-1) mod p
        s = pow(c1, self._x, self._p)
        s_inv = pow(s, -1, self._p)
        m = (c2 * s_inv) % self._p
        print(f"Déchiffrement : s = {c1}^{self._x} mod {self._p}\n\t\t= {s}")
        print(f"Déchiffrement : m = {c2} * {s_inv} mod {self._p}\n\t\t= {m}")
        return m


    def verify_private_key(self, x):
        if pow(self._g, x, self._p) == self._h:
            print(f"{x} est la clé privée car {self._g}^{x} mod {self._p} = {self._h}")
            self._x = x
        else:
            print(f"{x} n'est pas la clé privée car {self._g}^{x} mod {self._p} ≠ {self._h}")


    def brute_force_private_key(self):
        for x in range(1, self._p):  # x varie de 1 à p-1
            if pow(self._g, x, self._p) == self._h:
                self._x = x
                print(f"Clé privée retrouvée par brute force : x = {x}")
                return
        print("Aucune clé privée n'a été trouvée")
