## Requirements
To get started, make sure you have Python and install the required dependencies:
```py
pip install sympy
pip install pathlib
pip install unidecode
pip install ipykernel
```

**WARNING**  
The ```libaes.so``` library file located in ```algorithm/lib-c/``` may not be compatible with your computer due to architecture-specific compilation. To resolve this, you will need to get the source code of my AES implementation [**here**](https://github.com/Panegyrique/aes-c).

Open a terminal and compile the .so file using:
```bash
gcc -shared -o libaes.so -fPIC aes.c aes_display.c
```
Once compiled, place the ```libaes.so``` file into ```algorithm/lib-c/```.


## Function
```py
# AES
my_aes = AES()
my_aes.encrypt(plaintext, key)
my_aes.add_round_key(state, roundkey)
my_aes.sub_bytes(state)
my_aes.shift_rows(state)
my_aes.mix_columns(state)
my_aes.key_gen(master_key)

# CESAR
my_cesar = CESAR(k)
c = my_cesar.encrypt(m)
m = my_cesar.decrypt(c)

# DIFFIE_HELLMANN
my_diffie_hellmann = DIFFIE_HELLMANN(p, g)
k = my_diffie_hellmann.key_exchange(a, b)

# ECC
my_ecc = ECC(a, b, GF)
my_ecc.compute_points()
points = generate_curve_points(P=(xp, yp))
(xr, yr) = my_ecc.add_two_point(P=(xp, yp), Q=(xq, yq))
(xr, yr) = my_ecc.doubling_point(P=(xp, yp))
(xr, yr) = my_ecc.multiply_point(k, P=(xp, yp))
my_ecc.hasse_weil_borne()
r = my_ecc.try_generator_p(P=(xp, yp))
Kpu = my_ecc.compute_Kpu(Kpr)
sigma_1, sigma_2 = my_ecc.sign(hash_m, k, Kpr)
r = my_ecc.verif_sign(hash_m, sigma_1, sigma_2, Kpu)

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
r = my_basic_compute.modular_exponentiation(a, b, n,)
r = my_basic_compute.square_and_multiply(a, b, n,)
r = my_basic_compute.modular_square_root(a, n)
r = my_basic_compute.is_generator(group_order, g)
p, q = my_basic_compute.fermat_factorization(n)  
r = my_basic_compute.discrete_logarithm(a, b, n)
r = my_basic_compute.list_of_squares(x)

# LSFR
feedback_poly = [1, 0, 1, 0, 0]  # T^5 + T^2 + 1
initial_state = [1, 1, 1, 1, 1]
my_lfsr = LFSR(feedback_poly, initial_state)
my_lfsr.detect_period()
```