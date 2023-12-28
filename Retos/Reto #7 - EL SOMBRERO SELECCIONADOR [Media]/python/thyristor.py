"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""

def preguntar(pregunta, respuestas):
    print(pregunta)
    for i, respuesta in enumerate(respuestas, start=1):
        print(f"{i}. {respuesta}")
    
    while True:
        try:
            seleccion = int(input("Selecciona una opción (1-4): "))
            if 1 <= seleccion <= 4:
                return seleccion
            else:
                print("Selecciona un número válido.")
        except ValueError:
            print("Por favor, ingresa un número.")

def sombrero_seleccionador():
    rasgos = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    print("¡Bienvenido al Sombrero Seleccionador!")

    # Preguntas
    preguntas = [
        "¿Qué cualidad valoras más?",
        "¿Qué animal te gustaría tener como mascota?",
        "¿Qué asignatura te resulta más interesante?",
        "¿Qué harías si encuentras una llave encantada?",
        "¿Cuál es tu mayor miedo?",
    ]

    respuestas = [
        ["Valentía", "Ambición", "Lealtad", "Intelecto"],
        ["León", "Serpiente", "Tejón", "Águila"],
        ["Defensa Contra las Artes Oscuras", "Pociones", "Cuidado de Criaturas Mágicas", "Adivinación"],
        ["Intentaría abrirla con magia", "Buscaría ayuda", "Dejaría la llave", "Intentaría abrir la puerta sin la llave"],
        ["La soledad", "El fracaso", "La injusticia", "La ignorancia"],
    ]

    for i in range(5):
        seleccion = preguntar(preguntas[i], respuestas[i])
        for casa, puntaje in rasgos.items():
            rasgos[casa] += respuestas[i][seleccion - 1] == respuestas[i][puntaje]

    casa_seleccionada = max(rasgos, key=rasgos.get)
    print(f"\n¡Eres parte de la casa {casa_seleccionada}!")

if __name__ == "__main__":
    sombrero_seleccionador()