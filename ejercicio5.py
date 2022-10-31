from hashlib import sha256 

def encriptacion():
    c = str(input("Introduce el mensaje para encriptar: ")).encode("utf-8")
    encri = sha256(c).hexdigest()[:8]
    with open("encriptados.txt" , "w", encoding= "utf-8") as f:
        f.write(encri)


def desencriptacion():
    resolver = str(input("Hash a resolver: "))
    resolvedor = open("encriptados.txt", "r")
    for x in resolvedor.readlines():
        r = resolver.encode("utf-8")
        a= sha256(r).hexdigest()[:8]
        if a == r:
            with open("desencriptados.txt" , "a") as f:
                f.write(resolver)