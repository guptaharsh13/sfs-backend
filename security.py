import time
import math
from Crypto import Random
from Crypto.Cipher import DES3
import pyaes
import pbkdf2
import binascii
import os
import secrets


password = "some_random_password"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key -', binascii.hexlify(key))


iv = secrets.randbits(256)
to_encrypt = "Some random file to be encrypted"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(to_encrypt)
print('Encrypted -', binascii.hexlify(ciphertext))


aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('Decrypted - ', decrypted.decode())

# ---------------------------------------

time.clock = time.time

key = 'some random key '
iv = Random.new().read(DES3.block_size)
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
# padded with spaces so than len(to_encrypt) is multiple of 8
to_encrypt = 'Some random file to be encrypted'

to_encrypt = f"{to_encrypt}{' ' * ((math.ceil(len(to_encrypt) / 8) * 8) - len(to_encrypt))}"
encrypted_text = cipher_encrypt.encrypt(to_encrypt)
print("\n\n\n")
print(encrypted_text)
print("\n\n")

# you can't reuse an object for encrypting or decrypting other data with the same key.
cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv)
print(cipher_decrypt.decrypt(encrypted_text).decode())
cipher_decrypt.decrypt(encrypted_text)  # you cant do it twice
