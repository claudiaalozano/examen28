from hashlib import sha256 

def encriptacion():
    c = str(input("Introduce un mensaje de 8 caracteres para encriptar: ")).encode("utf-8")
    encri = sha256(c).hexdigest()
    with open("encriptados.txt" , "w", encoding= "utf-8") as f:
        f.write(encri)

        