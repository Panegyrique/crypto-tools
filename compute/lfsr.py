class LFSR:

    def __init__(self, poly, init):
        self._poly = poly
        self._init = init

    def compute_evol(self):
        state = self._init[:] 
        n = len(state)
        sequence = []
        state_tuples = set()  # Pour détecter la répétition des états

        print("\nÉvolution du LFSR :")

        t = 0
        while tuple(state) not in state_tuples:
            state_tuples.add(tuple(state))
            sequence.append(tuple(state))
            print(f"t:{t} state: {state}")

            feedback = 0
            for i in range(n):
                if self._poly[i] == 1:
                    feedback ^= state[i]

            state = [feedback] + state[:-1]
            t += 1

        print(f"Repetition : cycle achevé, la periode de la sequence est de {t}")
        return sequence

    def max_evol(self):
        max_period = 2**len(self._init) - 1
        print(f"\nPériode maximale possible : {max_period}")
        return max_period
    