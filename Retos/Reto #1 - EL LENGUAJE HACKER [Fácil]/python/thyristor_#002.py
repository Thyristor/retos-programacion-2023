#/*
# * Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.
# */

def funcion(string_1: str, string_2: str):
    if string_1 == string_2:
        print("Las dos palbras son iguales")
        return False
    elif string_1[::-1] == string_2:
        print("Es un anagrama")
        return True
    else:
        print("No es un anagrama")
        return False

if __name__ == "__main__":
    string_1 = input("Introduce el primer string: ")
    string_2 = input("Introduce el segundo string: ")

    booleano = funcion(string_1, string_2)
    print(f"Booleano: {booleano}")