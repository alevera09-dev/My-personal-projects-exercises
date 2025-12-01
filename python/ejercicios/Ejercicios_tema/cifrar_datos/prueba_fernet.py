from cryptography.fernet import Fernet
"""
key = Fernet.generate_key()

cifrar = Fernet(key)
desifrar = Fernet(key) 
contraseña = "210109@Vl"

contraseña_cifrada = cifrar.encrypt(contraseña.encode())

print(contraseña_cifrada)
print(key)

with open("keyfernet.bin", "ab") as archkey:
    archkey.write(key)
with open("passwords.enc", "ab") as archpass_word:
    archpass_word.write(contraseña_cifrada)    
"""
key = None    
with open("keyfernet.bin", "rb") as keybin:
    key = keybin.read()

password = None
with open("passwords.enc", "rb") as password_bin:
    password = password_bin.read()
    
desifrar = Fernet(key)

password_desifrada = desifrar.decrypt(password).decode()

print("Contraseña encriptada", password)
print("Contraseña desifrada:", password_desifrada)        