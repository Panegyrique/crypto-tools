## Function
``` python
# AES
my_aes = AES()
my_aes.encrypt(plaintext, key)

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

# CESAR
my_cesar = CESAR(k)
c = my_cesar.encrypt(m)
m = my_cesar.decrypt(c)

# VIGENERE
my_vigenere = VIGENERE(k)
c = my_vigenere.encrypt(m)
m = my_vigenere.decrypt(c)

# BASIC COMPUTE
my_basic_compute = BASIC_COMPUTE()
my_basic_compute.
```