import ctypes
from algorithm import AES, CESAR, DIFFIE_HELLMANN, ECC, ELGAMAL, RSA, VIGENERE
from compute import BASIC_COMPUTE


if __name__ == "__main__":

    # """
    #     AES
    # """
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

    # plaintext = (ctypes.c_uint8 * 16)(
    #     0x32, 0x88, 0x31, 0xe0, 
    #     0x43, 0x5a, 0x31, 0x37, 
    #     0xf6, 0x30, 0x98, 0x07, 
    #     0xa8, 0x8d, 0xa2, 0x34
    # )

    # key = (ctypes.c_uint8 * 16)(
    #     0x2b, 0x28, 0xab, 0x09, 
    #     0x7e, 0xae, 0xf7, 0xcf, 
    #     0x15, 0xd2, 0x15, 0x4f, 
    #     0x16, 0xa6, 0x88, 0x3c
    # )

    # state = (ctypes.c_uint8 * 16)(
    #     0x42, 0x00, 0x3a, 0x8e, 
    #     0x28, 0x6b, 0x0a, 0x6c, 
    #     0x03, 0xaa, 0x88, 0xbc, 
    #     0x4b, 0x27, 0x11, 0x60
    # )

    # state = (ctypes.c_uint8 * 16)(
    #     0x2c, 0x63, 0x80, 0x19, 
    #     0x34, 0x7f, 0x67, 0x50, 
    #     0x7b, 0xac, 0xc4, 0x65, 
    #     0xb3, 0xcc, 0x82, 0xd0
    # )
    
    # state = (ctypes.c_uint8 * 16)(
    #     0x2c, 0x63, 0x80, 0x19, 
    #     0x7f, 0x67, 0x50, 0x34, 
    #     0xc4, 0x65, 0x7b, 0xac, 
    #     0xd0, 0xb3, 0xcc, 0x82
    # )

    # my_aes = AES()
    # my_aes.encrypt(plaintext, key)
    # my_aes.add_round_key(plaintext, key)
    # my_aes.sub_bytes(state)
    # my_aes.shift_rows(state)
    # my_aes.mix_columns(state)
    # my_aes.key_gen(key)


    # """
    #     CESAR
    # """
    # my_cesar = CESAR(k=7)
    # m = my_cesar.decrypt("QLZBP ZHSVU KYLZK HUZBU LKLZY BLZSL ZWSBZ TPZLY HISLZ KLSHC PSSLQ LTHYJ OLLUT LKLTH UKHUA JVTTL UAZLK PABYP UVPYL UHUNS HPZ")
    # c = my_cesar.encrypt("jesui salon dresd ansun edesr uesle splus miser ables delav illej emarc heenm edema ndant comme ntsed ituri noire nangl ais")


    # """
    #     DIFFIE_HELLMANN
    # """
    # my_diffie_hellmann = DIFFIE_HELLMANN(p=59, g=2)
    # my_diffie_hellmann.key_exchange(5, 21)


    # """
    #     ECC
    # """
    # my_ecc = ECC(a=0, b=1, GF=5)
    # my_ecc.compute_points()
    # my_ecc.hasse_weil_borne()
    # my_ecc.try_generator_p((2,3))


    # """
    #     ELGAMAL
    # """
    # my_elgamal = ELGAMAL(p=101, g=7, h=44)

    # print("\n1. Recherche de la clé privée :")
    # my_elgamal.brute_force_private_key()

    # print("\n2. Que signifie '7 est un générateur' ?")
    # print("Cela signifie que 7 est un élément du groupe F101 qui peut générer tous les autres éléments du groupe multiplicatif modulo 101 via des puissances successives")

    # m = 89
    # k = 15
    # print("\n3. Calcul du chiffré pour m = 89 avec k = 15 :")
    # c1, c2 = my_elgamal.encrypt(m, k)

    # x = 35
    # print("\n4. Vérification que x = 35 est la clé privée :")
    # my_elgamal.verify_private_key(x)

    # print("\n5. Déchiffrement du texte chiffré pour retrouver le texte clair :")
    # m = my_elgamal.decrypt(c1, c2)


    # """
    #     RSA
    # """
    # my_rsa = RSA(n=493, e=33)

    # m1 = 110
    # print("1. Calcul du chiffré c1 pour m1 = 110 : ")
    # c1 = my_rsa.encrypt(m1)

    # p = 17
    # print("\n2. Vérification que p = 17 est un facteur de n :")
    # my_rsa.check_factor_p(p)

    # print("\n3. Calcul de ϕ(n) :")
    # my_rsa.found_phi_n()

    # print("\n4. Calcul de l'exposant de déchiffrement d :")
    # my_rsa.found_d()

    # c2 = 335
    # print("\n5. Calcul du message clair m2 pour le chiffré c2 = 335 :")
    # m2 = my_rsa.decrypt(c2)

    # print("\n6. Recherche de la clé de déchiffrement d par brute force :")
    # my_rsa.brute_force_d()


    # """
    #     VIGENERE
    # """
    # my_vigenere = VIGENERE(k="Miaou")
    # c = my_vigenere.encrypt("As tu un animal de compagnie ?")
    # m = my_vigenere.decrypt("Aci ih pqpzipwcim viuby.")


    """
        BASIC COMPUTE
    """
    compute = BASIC_COMPUTE()
    # r, _ = compute.pgcd(15, 4)
    # r = compute.euclide_extended(66, 17)
    # r = compute.modular_exponentiation(2, 7, 55)
    # r = compute.square_and_multiply(18, 23, 55)
    # r = compute.modular_square_root(1, 77)
    # r = compute.primality_test(55)
    # r = compute.is_generator(59-1, 2)
    # p, q = compute.fermat_factorization(3917299) 
    # r = compute.discrete_logarithm(2, 11, 59)