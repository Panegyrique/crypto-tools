import ctypes
from algorithm import AES, ELGAMAL, RSA, CESAR, VIGENERE
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
    
    # my_aes = AES()
    # my_aes.encrypt(plaintext, key)


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
    #     CESAR
    # """
    # my_cesar = CESAR(k=7)
    # m = my_cesar.decrypt("QLZBP ZHSVU KYLZK HUZBU LKLZY BLZSL ZWSBZ TPZLY HISLZ KLSHC PSSLQ LTHYJ OLLUT LKLTH UKHUA JVTTL UAZLK PABYP UVPYL UHUNS HPZ")
    # c = my_cesar.encrypt("jesui salon dresd ansun edesr uesle splus miser ables delav illej emarc heenm edema ndant comme ntsed ituri noire nangl ais")


    """
        VIGENERE
    """
    my_vigenere = VIGENERE(k="Miaou")
    c = my_vigenere.encrypt("As tu un animal de compagnie ?")
    m = my_vigenere.decrypt("Aci ih pqpzipwcim viuby.")