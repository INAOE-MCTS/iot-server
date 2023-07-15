from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode


def cipher_asimetric(key):

    # Cargar llave publica del cliente
    public_key = RSA.import_key(key)
    session_key = get_random_bytes(32)

    # Encriptar llave de sesion con llave publica del cliente
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    session_key = b64encode(session_key).decode('utf-8')
    print("clave de sesion en base64: ")
    print(session_key)

    enc_session_key = b64encode(enc_session_key).decode('utf-8')
    print("clave de sesion encryptada: ")
    print(enc_session_key)

    if enc_session_key:
        return session_key, enc_session_key
    else:
        return None


def descipher_asimetric(data):

    # Cargar llave privada del servidor
    private_key = RSA.import_key(open("private.pem").read())

    # Se lee la data cifrada 
    deschipher_rsa = PKCS1_OAEP.new(private_key)
    data_decrypted = deschipher_rsa.decrypt(data)
    print("Data decifrada: ")
    print(data_decrypted)

    if data_decrypted:
        return data_decrypted
    else:
        return None

# print(chipher_asimetric(open("public.pem").read()))
cipher_asimetric(open("public.pem").read())