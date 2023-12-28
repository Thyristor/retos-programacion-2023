"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string

def generar_contraseña(longitud, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_letters if mayusculas else string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    print("Generador de Contraseñas Aleatorias")
    longitud = int(input("Longitud de la contraseña (entre 8 y 16): "))
    
    if 8 <= longitud <= 16:
        mayusculas = input("Incluir letras mayúsculas (S/N): ").lower() == 's'
        numeros = input("Incluir números (S/N): ").lower() == 's'
        simbolos = input("Incluir símbolos (S/N): ").lower() == 's'
        
        contraseña = generar_contraseña(longitud, mayusculas, numeros, simbolos)
        print("Contraseña generada:", contraseña)
    else:
        print("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")