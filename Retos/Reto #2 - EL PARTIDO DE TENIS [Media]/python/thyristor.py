#/*
# * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# * gane cada punto del juego.
# * 
# * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# *   15 - Love
# *   30 - Love
# *   30 - 15
# *   30 - 30
# *   40 - 30
# *   Deuce
# *   Ventaja P1
# *   Ha ganado el P1
# * - Si quieres, puedes controlar errores en la entrada de datos.   
# * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
# */

sequence = ("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")
total_p1 = sequence.count("P1")
total_p2 = sequence.count("P2")

if total_p1 + total_p2 != len(sequence) or abs(total_p1 - total_p2) >= 3:
    print("Error secuencia")

match = ("Love", "15", "30", "40")
p1_pts = 0
p2_pts = 0
for s in sequence:
    if s == "P1":
        p1_pts += 1
    elif s == "P2":
        p2_pts += 1

    if (p1_pts >= 4 or p2_pts >= 4):
        if (p1_pts == p2_pts):
            print("Deuce")
        elif (p1_pts - p2_pts >= 2):
            print("Ha ganado P1")
        elif (p2_pts - p1_pts >= 2):
            print("Ha ganado P2")
        elif (p1_pts > p2_pts):
            print("Ventaja P1")
        elif (p1_pts < p2_pts):
            print("Ventaja P2")
    else:
        if (p1_pts == 3 and p2_pts == 3):
            print("Deuce")
        else:
            print(f"{match[p1_pts]} - {match[p2_pts]}")