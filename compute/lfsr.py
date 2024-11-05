class LFSR:
    def __init__(self, poly):
        self._poly = poly  # Le polynôme de rétroaction, sous forme de liste de coefficients (1 ou 0)

    def compute_evol(self, init, display=True):
        state = init[:]  # Copie de l'état initial
        n = len(state)
        sequence = []
        state_tuples = set()  # Pour détecter la répétition des états

        if display:
            print("\nÉvolution du LFSR :")

        t = 0
        while tuple(state) not in state_tuples:
            # Ajoute l'état courant à la séquence et l'affiche
            state_tuples.add(tuple(state))
            sequence.append(tuple(state))
            if display:
                print(f"t:{t} state: {state}")

            # Calcul du bit de rétroaction
            feedback = 0
            for i in range(n):  # Boucle uniquement sur les indices valides de state
                if self._poly[i] == 1:
                    feedback ^= state[i]

            # Décalage à droite et ajout du bit de rétroaction
            state = [feedback] + state[:-1]
            t += 1

        # Affiche la période une fois que la séquence devient périodique
        if display:
            print(f"Repetition : cycle is achieved, period of sequence of states is {t}")

        return sequence

    def max_evol(self, display=True):
        # La période maximale possible est 2^n - 1
        max_period = 2**len(self._poly) - 1
        if display:
            print(f"\nPériode maximale possible : {max_period}")
        return max_period