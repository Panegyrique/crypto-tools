from compute.basic_compute import BASIC_COMPUTE

class DIFFIE_HELLMANN:
    
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def key_exchange(self, a, b):
        print(f"\nInitialisation de l'échange de clés Diffie-Hellman avec:")
        print(f"\tNombre premier p = {self.p}")
        print(f"\tGénérateur g = {self.g}")
        print(f"\tSecrets choisis a = {a}, b = {b}")
        my_basic_compute = BASIC_COMPUTE()

        print("\nCalcul des valeurs publiques A = (g^a mod p) et B = (g^b mod p):", end='')
        A = my_basic_compute.modular_exponentiation(self.g, a, self.p)
        print(f"\t=> A = (g^a mod p) = {A}")
        B = my_basic_compute.modular_exponentiation(self.g, b, self.p)
        print(f"\t=> B = (g^b mod p) = {B}")

        print("\nÉchange des valeurs publiques:")
        print(f"\tAlice envoie A = {A}")
        print(f"\tBob envoie B = {B}")

        print("\nCalcul de la clé secrète partagée K1 = (B^a mod p) et K2 = (A^b mod p):", end='')
        K1 = my_basic_compute.modular_exponentiation(B, a, self.p)
        print(f"\t=> Alice calcule K1 = B^a mod p = {K1}")
        K2 = my_basic_compute.modular_exponentiation(A, b, self.p)
        print(f"\t=> Bob calcule K2 = A^b mod p = {K2}")

        if K1 == K2:
            print("\n=> Échange de clés réussi K1 = K2. Clé secrète partagée:", K1)
        else:
            print("\n=> Échange de clés échoué K1 != K2. Les clés ne correspondent pas.")

        return K1
