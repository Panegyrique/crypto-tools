from compute.basic_compute import BASIC_COMPUTE

class RSA:
    
    def __init__(self, n, e, d=None, p=None, q=None):
        self._n = n
        self._e = e
        self._d = d

        self._p = p
        self._q = q
        self._phi_n = None

        self._compute = BASIC_COMPUTE()

    def encrypt(self, m):
        # c = m^e mod n
        c = self._compute.square_and_multiply(m, self._e, self._n)
        return c

    def decrypt(self, c):
        # m = c^d mod n
        if self._d is None:
            print("Erreur : L'exposant de déchiffrement d n'est pas encore défini.")
            return None
        m = self._compute.square_and_multiply(c, self._d, self._n)
        return m

    def check_factor_p(self, p):
        if self._n % p == 0:
            self._p = p
            self._q = self._n // p
            print(f"{p} est un facteur de {self._n} car n % p == 0\nq = n / p = {self._q}")
        else:
            print(f"{p} n'est pas un facteur de {self._n}.")

    def check_factor_q(self, q):
        if self._n % q == 0:
            self._q = q
            self._p = self._n // q
            print(f"{q} est un facteur de {self._n} car n % p == 0\np = n / q = {self._p}")
        else:
            print(f"{q} n'est pas un facteur de {self._n}.")

    def found_phi_n(self):
        # ϕ(n) = (p - 1) * (q - 1)
        if self._p and self._q:
            self._phi_n = (self._p - 1) * (self._q - 1)
            print(f"Calcul de ϕ(n) : (p-1) * (q-1) = ({self._p}-1) * ({self._q}-1) = {self._phi_n}\nϕ(n) = {self._phi_n}")
        else:
            print("Impossible de calculer ϕ(n) sans les facteurs p et q de n")

    def found_d(self):
        # d * e ≡ 1 (mod ϕ(n)) en utilisant l'algorithme d'Euclide étendu
        print("Début du calcul de d (appelé a par la suite) tel que d * e ≡ 1 (mod ϕ(n)) :")
        if self._phi_n is None:
            print("Erreur : ϕ(n) n'est pas défini. Veuillez calculer ϕ(n) avant de chercher d.")
            return
        gcd = self._compute.euclide_extended(self._e, self._phi_n)

    def brute_force_d(self):
        self._d = None
        if self._phi_n is None:
            print("Erreur : ϕ(n) n'est pas défini. Veuillez calculer ϕ(n) avant d'utiliser la méthode brute force.")
        
        for d in range(1, self._phi_n):  # d varie de 1 à ϕ(n)-1
            if (d * self._e) % self._phi_n == 1:
                self._d = d
                print(f"Clé de déchiffrement trouvée par brute force : d = {d}")
                return
        print("Aucune clé de déchiffrement n'a été trouvée.")
