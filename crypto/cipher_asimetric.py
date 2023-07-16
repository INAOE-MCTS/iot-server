from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode


def cipher_asimetric(key):

    print(type(key))
    # Cargar llave publica del cliente
    public_key = RSA.import_key(key)
    session_key = get_random_bytes(32)
    print(session_key)

    # Encriptar llave de sesion con llave publica del cliente
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    session_key = b64encode(session_key).decode('utf-8')
    # print("clave de sesion en base64: ")
    # print(session_key)

    enc_session_key = b64encode(enc_session_key).decode('utf-8')
    # print("clave de sesion encryptada: ")
    # print(enc_session_key)

    if enc_session_key:
        return session_key, enc_session_key
    else:
        return None


def descipher_asimetric(data):

    print(data)
    # Cargar llave privada del servidor
    private_key = RSA.import_key(open("./crypto/private.pem").read())

    data_encode = data.encode('utf-8')
    print(data_encode)
    
    data = b64decode(data_encode)
    print(data)


    # Se lee la data cifrada 
    deschipher_rsa = PKCS1_OAEP.new(private_key)
    data_decrypted = deschipher_rsa.decrypt(data)

    if data_decrypted:
        return data_decrypted
    else:
        return None

