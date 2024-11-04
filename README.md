## Dependencies
```py
pip install sympy
pip install pathlib
pip install unidecode
```

## Function
```py
# AES
my_aes = AES()
my_aes.encrypt(plaintext, key)

# CESAR
my_cesar = CESAR(k)
c = my_cesar.encrypt(m)
m = my_cesar.decrypt(c)

# ECC
my_ecc = ECC(a, b, GF)
my_ecc.compute_points()
my_ecc.add_two_point(P=(xp, yp), Q=(xq, yq))
my_ecc.doubling_point(P=(xp, yp))
my_ecc.hasse_weil_borne()
my_ecc.try_generator_p(P=(xp, yp))

# ELGAMAL
my_elgamal = ELGAMAL(p, g, h, x=None)
c1, c2 = my_elgamal.encrypt(m, k)
m = my_elgamal.decrypt(c1, c2)
my_elgamal.verify_private_key(x)
my_elgamal.brute_force_private_key()

# RSA
my_rsa = RSA(n, e, d=None, p=None, q=None)
c = my_rsa.encrypt(m)
m = my_rsa.decrypt(c)
my_rsa.check_factor_p(p)
my_rsa.check_factor_q(q)
my_rsa.found_phi_n()
my_rsa.found_d()
my_rsa.brute_force_d()

# VIGENERE
my_vigenere = VIGENERE(k)
c = my_vigenere.encrypt(m)
m = my_vigenere.decrypt(c)

# BASIC COMPUTE
my_basic_compute = BASIC_COMPUTE()
r, _ = my_basic_compute.pgcd(a, b)
r = my_basic_compute.euclide_extended(a, n)
r = my_basic_compute.modular_exponentiation(a, b, n, display=True)
r = my_basic_compute.square_and_multiply(a, b, n, display=True)
r = my_basic_compute.modular_square_root(a, n)
r = my_basic_compute.is_generator(group_order, g)
```