import ctypes
from pathlib import Path

DATA_SIZE = 16            # Size of the data block (for AES-128)
STATE_ROW_SIZE = 4        # Number of rows in the state matrix
STATE_COL_SIZE = 4        # Number of columns in the state matrix
ROUND_COUNT = 10          # Number of rounds for AES-128

class AES:
    
    def __init__(self):
        path_file_c = Path(__file__).parent / 'lib-c/libaes.so'
        self.aes_lib = ctypes.CDLL(str(path_file_c))

        self.aes_lib.AESEncryptDisplay.argtypes = (
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8)
        )
        self.aes_lib.AESEncryptDisplay.restype = None

        self.aes_lib.AddRoundKeyDisplay.argtypes = (
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE), 
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE)
        )
        self.aes_lib.AddRoundKeyDisplay.restype = None

        self.aes_lib.SubBytesDisplay.argtypes = (
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE),
        )
        self.aes_lib.SubBytesDisplay.restype = None

        self.aes_lib.ShiftRowsDisplay.argtypes = (
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE),
        )
        self.aes_lib.ShiftRowsDisplay.restype = None

        self.aes_lib.MixColumnsDisplay.argtypes = (
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE),
        )
        self.aes_lib.MixColumnsDisplay.restype = None

        self.aes_lib.KeyGenDisplay.argtypes = (
            (ctypes.c_uint8 * ((ROUND_COUNT + 1) * STATE_ROW_SIZE * STATE_COL_SIZE)),  # 11 keys for AES-128 (10 rounds + 1)
            (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE)
        )
        self.aes_lib.KeyGenDisplay.restype = None

    def encrypt(self, plaintext, key):
        ciphertext = (ctypes.c_uint8 * DATA_SIZE)()
        self.aes_lib.AESEncryptDisplay(ciphertext, plaintext, key)

    def add_round_key(self, state, roundkey):
        state_send = self._message_to_state(state)
        roundkey_send = self._message_to_state(roundkey)
        self.aes_lib.AddRoundKeyDisplay(state_send, roundkey_send)

    def sub_bytes(self, state):
        state_send = self._message_to_state(state)
        self.aes_lib.SubBytesDisplay(state_send)

    def shift_rows(self, state):
        state_send = self._message_to_state(state)
        self.aes_lib.ShiftRowsDisplay(state_send)

    def mix_columns(self, state):
        state_send = self._message_to_state(state)
        self.aes_lib.MixColumnsDisplay(state_send)

    def key_gen(self, state):
        # Create a buffer for 11 round keys
        master_key = self._message_to_state(state)
        roundkeys = (ctypes.c_uint8 * ((ROUND_COUNT + 1) * STATE_ROW_SIZE * STATE_COL_SIZE))()  
        self.aes_lib.KeyGenDisplay(roundkeys, master_key)
    
    def _message_to_state(self, message):
        state = (ctypes.c_uint8 * STATE_ROW_SIZE * STATE_COL_SIZE)()
        for i in range(STATE_ROW_SIZE):
            for j in range(STATE_COL_SIZE):
                state[i][j] = message[i * STATE_COL_SIZE + j]
        return state
