import ctypes
from algorithm import AES, CESAR, DIFFIE_HELLMANN, ECC, ELGAMAL, RSA, VIGENERE
from compute import BASIC_COMPUTE, LFSR


if __name__ == "__main__":

    """
        AES
    """
    # plaintext = (ctypes.c_uint8 * 16)(
    #     0x00, 0x44, 0x88, 0xcc, 
    #     0x11, 0x55, 0x99, 0xdd, 
    #     0x22, 0x66, 0xaa, 0xee, 
    #     0x33, 0x77, 0xbb, 0xff
    # )

    # key = (ctypes.c_uint8 * 16)(
    #     0x00, 0x04, 0x08, 0x0c, 
    #     0x01, 0x05, 0x09, 0x0d, 
    #     0x02, 0x06, 0x0a, 0x0e, 
    #     0x03, 0x07, 0x0b, 0x0f
    # )

    # state = (ctypes.c_uint8 * 16)(
    #     0x42, 0x00, 0x3a, 0x8e, 
    #     0x28, 0x6b, 0x0a, 0x6c, 
    #     0x03, 0xaa, 0x88, 0xbc, 
    #     0x4b, 0x27, 0x11, 0x60
    # )

    # my_aes = AES()
    # my_aes.encrypt(plaintext, key)
    # my_aes.add_round_key(plaintext, key)
    # my_aes.sub_bytes(state)
    # my_aes.shift_rows(state)
    # my_aes.mix_columns(state)
    # my_aes.key_gen(key)


    """
        CESAR
    """
    # my_cesar = CESAR(k=7)
    # _ = my_cesar.encrypt(m="jesui salon dresd ansun edesr uesle splus miser ables delav illej emarc heenm edema ndant comme ntsed ituri noire nangl ais")
    # _ = my_cesar.decrypt(c="QLZBP ZHSVU KYLZK HUZBU LKLZY BLZSL ZWSBZ TPZLY HISLZ KLSHC PSSLQ LTHYJ OLLUT LKLTH UKHUA JVTTL UAZLK PABYP UVPYL UHUNS HPZ")


    """
        DIFFIE_HELLMANN
    """
    # my_diffie_hellmann = DIFFIE_HELLMANN(p=59, g=2)
    # _ = my_diffie_hellmann.key_exchange(a=5, b=21)


    """
        ECC
    """
    # my_ecc = ECC(a=2, b=1, GF=5)
    # my_ecc.compute_points()
    # _ = my_ecc.add_two_point(P=(0,1), Q=(1,2))
    # _ = my_ecc.doubling_point(P=(0,1))
    # _ = my_ecc.multiply_point(k, P=(xp, yp))
    # my_ecc.hasse_weil_borne()
    # _ = my_ecc.try_generator_p(P=(0,1))
    # _ = my_ecc.compute_Kpu(Kpr=2)
    # _, _ = my_ecc.sign(hash_m=4, k=3, Kpr=2)
    # _ = my_ecc.verif_sign(hash_m=4, sigma_1=3, sigma_2=1, Kpu=(1, 3))


    """
        ELGAMAL
    """
    # my_elgamal = ELGAMAL(p=101, g=7, h=44)
    # my_elgamal.brute_force_private_key()
    # r = my_elgamal.verify_private_key(x=35)
    # c1, c2 = my_elgamal.encrypt(m=89, k=15)
    # _ = my_elgamal.decrypt(c1, c2)


    """
        RSA
    """
    # my_rsa = RSA(n=493, e=33)
    # c1 = my_rsa.encrypt(m=110)
    # my_rsa.check_factor_p(p=17)
    # my_rsa.found_phi_n()
    # my_rsa.found_d()
    # m = my_rsa.decrypt(c1)
    # my_rsa.brute_force_d()


    """
        VIGENERE
    """
    # my_vigenere = VIGENERE(k="Miaou")
    # c = my_vigenere.encrypt(m="As tu un animal de compagnie ?")
    # m = my_vigenere.decrypt(c="Aci ih pqpzipwcim viuby.")


    """
        BASIC COMPUTE
    """
    # compute = BASIC_COMPUTE()
    # r, _ = compute.pgcd(15, 4)
    # r = compute.euclide_extended(66, 17)
    # r = compute.modular_exponentiation(2, 7, 55)
    # r = compute.square_and_multiply(18, 23, 55)
    # r = compute.modular_square_root(1, 77)
    # r = compute.primality_test(55)
    # r = compute.is_generator(113-1, 3)
    # p, q = compute.fermat_factorization(3917299) 
    # r = compute.discrete_logarithm(3, 57, 113, 112)
    # r = compute.list_of_squares(11)


    """
        LFSR
    """
    # my_lfsr = LFSR(poly = [1, 0, 0, 1, 1], init = [1, 0, 0, 1])             # Polynôme x^4 + x + 1
    # sequence = my_lfsr.compute_evol()
    # max_period = my_lfsr.max_evol()
