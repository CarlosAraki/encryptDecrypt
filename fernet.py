import sys
from cryptography.fernet import Fernet

if len(sys.argv) != 4:
    print("Argumentos inválidos: e/d,string,key",(sys.argv))
else:
    key = sys.argv[3]
    message = sys.argv[2]
    if sys.argv[1] == 'e' :
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())
        print("encrypted string: ", encMessage)
        print("key string: ", key)
        key = Fernet.generate_key()

    else:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        decMessage = fernet.decrypt(message).decode()
        print("decrypted string: ", decMessage)