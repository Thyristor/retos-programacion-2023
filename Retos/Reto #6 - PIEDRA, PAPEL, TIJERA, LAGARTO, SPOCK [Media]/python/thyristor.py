"""
Crea un programa que calcule quien gana mas partidas al piedra,
papel, tijera, lagartija, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La funcion recibe un listado que contiene pares,
representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄"
(papel), 
"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. 
Resultado: "Player 2".
"""

def determinar_ganador(partidas):
    reglas = {
        ("🗿", "✂️"): "Player 1",
        ("✂️", "🗿"): "Player 2",
        ("📄", "✂️"): "Player 2",
        ("✂️", "📄"): "Player 1",
        ("🗿", "📄"): "Player 2",
        ("📄", "🗿"): "Player 1",
        ("✂️", "🦎"): "Player 1",
        ("🦎", "✂️"): "Player 2",
        ("🦎", "🗿"): "Player 1",
        ("🗿", "🦎"): "Player 2",
        ("📄", "🦎"): "Player 1",
        ("🦎", "📄"): "Player 2",
        ("🖖", "✂️"): "Player 1",
        ("✂️", "🖖"): "Player 2",
        ("🖖", "🗿"): "Player 1",
        ("🗿", "🖖"): "Player 2",
        ("📄", "🖖"): "Player 1",
        ("🖖", "📄"): "Player 2",
        ("🦎", "🖖"): "Player 1",
        ("🖖", "🦎"): "Player 2",
        ("🖖", "🖖"): "Tie",
        ("🦎", "🦎"): "Tie",
        ("📄", "📄"): "Tie",
        ("✂️", "✂️"): "Tie",
        ("🗿️", "🗿️"): "Tie",
    }

    contador = {"Player 1": 0, "Player 2": 0, "Tie": 0}

    for jugada in partidas:
        resultado = reglas.get(jugada)
        contador[resultado] += 1

    if contador["Player 1"] > contador["Player 2"]:
        return "Player 1"
    elif contador["Player 2"] > contador["Player 1"]:
        return "Player 2"
    else:
        return "Tie"

if __name__ == "__main__":
    partidas_ejemplo = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
    resultado = determinar_ganador(partidas_ejemplo)
    print("El ganador es:", resultado)