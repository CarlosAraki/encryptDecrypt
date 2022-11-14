import sys
from cryptography.fernet import Fernet
import base64


def Encrypt(text_f,f):
    encrypted = f.encrypt(bytes(text_f, 'utf-8'))
    return encrypted

def Decrypt(text_f,f):
    plain = f.decrypt(bytes(text_f, 'utf-8'))
    return plain

if len(sys.argv) > 4:
    print("Argumentos inválidos: e/d,string",(sys.argv))
else:
    message = sys.argv[2]
    if sys.argv[1] == 'e' :
        key = Fernet.generate_key()
        fernet = Fernet(key)
        print("encrypted string: ", Encrypt(message,fernet).decode("utf-8") )
        print("key string: ", key.decode("utf-8") )
    else:
        key = sys.argv[3]
        fernet = Fernet(key)
        print("decrypted string: ", Decrypt(message,fernet).decode("utf-8") )

