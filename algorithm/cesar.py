import unidecode

class CESAR():

    def __init__(self, k):
        self._k = k
        self._alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def encrypt(self, m):
        c = list(unidecode.unidecode(m.lower()))
        for i, letter in enumerate(c):
            if letter in [' ', ',', ';', ':', '.', '!', '?']:
                continue
            if letter in self._alphabet:
                c[i] = self._alphabet[((self._alphabet.index(letter) + self._k)%26)]
            else:
                break
        print(f"Message en clair : {m}\nMessage chiffré avec pour cle {self._k} (valeur du décalage) : {"".join(c)}")
        return "".join(c)
    
    def decrypt(self, c):
        m = list(unidecode.unidecode(c.lower()))
        for i, letter in enumerate(m):
            if letter in [' ', ',', ';', ':', '.', '!', '?']:
                continue
            if letter in self._alphabet:
                m[i] = self._alphabet[((self._alphabet.index(letter) - self._k)%26)]
            else:
                break
        print(f"Message chiffré : {c}\nMessage en clair avec pour cle {self._k} (valeur du décalage) : {"".join(m)}")
        return "".join(m)