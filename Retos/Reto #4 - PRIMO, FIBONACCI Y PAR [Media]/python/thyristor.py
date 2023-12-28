"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

def es_par(numero):
    return (numero % 2 == 0)

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    es_primo_resultado = es_primo(numero)
    es_fibonacci_resultado = es_fibonacci(numero)
    es_par = es_par(numero)

    resultado_primo = "primo" if es_primo_resultado else "no es primo"
    resultado_fibonacci = "fibonacci" if es_fibonacci_resultado else "no es fibonacci"
    resultado_par = "par" if es_par else "impar"

    resultado_final = f"{numero} es {resultado_primo}, {resultado_fibonacci} y es {resultado_par}"
    print(resultado_final)