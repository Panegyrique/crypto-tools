import unidecode

class VIGENERE():

    def __init__(self, k):
        self._k = unidecode.unidecode(k.lower())
        self._alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def encrypt(self, m):
        c = list(unidecode.unidecode(m.lower()))
        key_index = 0
        for i, letter in enumerate(c):
            if letter in [' ', ',', ';', ':', '.', '!', '?']:
                continue
            c[i] = self._alphabet[((self._alphabet.index(letter) + self._alphabet.index(self._k[key_index%len(self._k)]))%26)]
            key_index += 1
        print(f'Message en clair : {m}\nMessage chiffré avec pour cle "{self._k}" : {"".join(c)}')
        return "".join(c)
    
    def decrypt(self, c):
        m = list(unidecode.unidecode(c.lower()))
        key_index = 0
        for i, letter in enumerate(m):
            if letter in [' ', ',', ';', ':', '.', '!', '?']:
                continue
            m[i] = self._alphabet[((self._alphabet.index(letter) - self._alphabet.index(self._k[key_index%len(self._k)]))%26)]
            key_index += 1
        print(f'Message chiffré : {c}\nMessage en clair avec pour cle "{self._k}" : {"".join(m)}')
        return "".join(m)
