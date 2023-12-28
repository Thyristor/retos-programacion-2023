"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""

def es_heterograma(cadena):
    """
    Verifica si la cadena es un heterograma, es decir, si no contiene caracteres repetidos.
    """
    caracteres_vistos = set()

    for caracter in cadena:
        if caracter.isalpha():
            if caracter.lower() in caracteres_vistos:
                return False
            caracteres_vistos.add(caracter.lower())

    return True

def es_isograma(cadena):
    """
    Verifica si la cadena es un isograma, es decir, si no contiene letras repetidas.
    """
    letras_vistas = set()

    for letra in cadena:
        if letra.isalpha():
            if letra.lower() in letras_vistas:
                return False
            letras_vistas.add(letra.lower())

    return True

def es_pangrama(cadena):
    """
    Verifica si la cadena es un pangrama, es decir, si contiene todas las letras del alfabeto al menos una vez.
    """
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")

    for letra in cadena:
        if letra.isalpha():
            alfabeto.discard(letra.lower())

    return not bool(alfabeto)

if __name__ == "__main__":
    # Ejemplos de uso
    cadena_heterograma = "abcdefgh%$!¿?¡"
    cadena_isograma = "abcde"
    cadena_pangrama = "The quick brown fox jumps over the lazy dog"

    print("Es heterograma:", es_heterograma(cadena_heterograma))
    print("Es isograma:", es_isograma(cadena_isograma))
    print("Es pangrama:", es_pangrama(cadena_pangrama))