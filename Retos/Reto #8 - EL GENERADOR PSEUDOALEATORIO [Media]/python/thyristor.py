"""
* Crea un generador de números pseudoaleatorios entre 0 y 100.
* - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
*
* Es más complicado de lo que parece...
"""

class GeneradorPseudoaleatorio:
    def __init__(self, semilla):
        self.semilla = semilla

    def generar_numero(self):
        # Fórmula simple de generación pseudoaleatoria
        a = 1664525
        c = 1013904223
        m = 2**32
        self.semilla = (a * self.semilla + c) % m

        # Ajusta el rango para obtener un número entre 0 y 100
        numero_aleatorio = self.semilla % 101
        return numero_aleatorio

if __name__ == "__main__":
    # Ejemplo de uso
    semilla_inicial = int(input("Ingresa una semilla inicial: "))
    generador = GeneradorPseudoaleatorio(semilla_inicial)

    for _ in range(10):  # Genera 10 números pseudoaleatorios
        print(generador.generar_numero())