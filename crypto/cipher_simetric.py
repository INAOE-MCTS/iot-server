from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

session_key = "cloyYASLV4nOBlWQ5ITfbqVuQ3C8FLeQLM8TtujEF28="


def cipher_simetric(plaintext, session_key):

    plaintext_encode = plaintext.encode('utf-8')
    # Ciframos la data con la llave de sesion generada 
    key_encode = session_key.encode('utf-8')
    key = b64decode(key_encode)

    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(plaintext_encode, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ciphertext = b64encode(ct).decode('utf-8')

    # Retornamos la data cifrada y el vector de iniciacion cifrado en base64
    return ciphertext, iv



def descipher_simetric(ciphertext, iv, session_key):

    ciphertext_encode = ciphertext.encode('utf-8')
    ciphertext = b64decode(ciphertext_encode)

    iv_encode = iv.encode('utf-8')
    iv = b64decode(iv_encode)

    key_encode = session_key.encode('utf-8')
    key = b64decode(key_encode)

    # Desciframos la data con la llave de sesion generada y el vector de iniciacion
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext.decode('utf-8')

    # Retornamos la data descifrada en texto claro
    return plaintext

