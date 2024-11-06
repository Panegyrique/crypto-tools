class LFSR:

    def __init__(self, poly, init):
        self.feedback_poly = poly
        self.initial_state = init 
        self.state = init.copy()
        self.size = len(init)

    def _reset(self):
        self.state = self.initial_state.copy()

    def _calculate_feedback(self):
        feedback = 0
        for i, coef in enumerate(self.feedback_poly):
            if coef == 1:
                feedback ^= self.state[i]
        return feedback

    def _step(self):
        output_bit = self.state[0] # Le bit de sortie est le premier bit de l'état
        feedback = self._calculate_feedback() # Calculer le bit de rétroaction
        self.state = self.state[1:] + [feedback] # Décalage à gauche
        return output_bit

    def detect_period(self):
        self._reset()
        t = 0
        seen = set()

        polynomial_str = ""
        for i, bit in enumerate(self.feedback_poly):
            if bit == 1:
                if polynomial_str:
                    polynomial_str += " + "
                if i != 0:
                    polynomial_str += f"T^{i}"
                else:
                    polynomial_str += "1"
        polynomial_str += " + T^" + str(len(self.feedback_poly))
        print(f"Polynôme de rétroaction: {polynomial_str} (coefficients: {self.feedback_poly})")
        print(f"État initial: {self.state}")
        
        while tuple(self.state) not in seen:
            seen.add(tuple(self.state))
            output_bit = self._step()
            t += 1
            print(f"t:{t}  state: {self.state}  output bit: {output_bit}")

        print(f"\nPeriode maximale theorique: 2^(dim_init) - 1 = 2^{len(self.initial_state)} - 1\n\t=> {2 ** (len(self.initial_state)) - 1}")
