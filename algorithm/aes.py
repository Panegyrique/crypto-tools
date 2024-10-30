import ctypes
from pathlib import Path


class AES():
    
    def __init__(self):
        path_file_c = Path(__file__).parent / 'lib-c/libaes.so'
        self.aes_lib = ctypes.CDLL(str(path_file_c))

        self.aes_lib.AESEncryptDisplay.argtypes = (
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8)
        )
        self.aes_lib.AESEncryptDisplay.restype = None

        self.aes_lib.AESEncrypt.argtypes = (
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8), 
            ctypes.POINTER(ctypes.c_uint8)
        )
        self.aes_lib.AESEncrypt.restype = None
        
    def encrypt(self, plaintext, key):
        ciphertext = (ctypes.c_uint8 * 16)()
        self.aes_lib.AESEncryptDisplay(ciphertext, plaintext, key)
    