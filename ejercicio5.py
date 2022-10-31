from hashlib import sha256 

def encriptacion(c, resolver):
   
    encri = sha256(c).hexdigest()[:8]
    with open("encriptados.txt" , "w", encoding= "utf-8") as f:
        f.write(encri)
    
    resolvedor = encri
    for x in resolvedor:
        r = resolver.encode("utf-8")
        a= sha256(r).hexdigest()[:8]
        if a == resolvedor:
            with open("desencriptados.txt" , "w") as f:
                f.write(resolver)
        else: 
            print("Las claves no coinciden.")

