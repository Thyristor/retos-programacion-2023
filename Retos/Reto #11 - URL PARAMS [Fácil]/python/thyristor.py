"""
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

def obtener_parametros_url(url):
    parametros = []
    en_parametros = False
    valor_actual = ""

    for caracter in url:
        if caracter == "?":
            en_parametros = True
        elif en_parametros and caracter in ["=", "&"]:
            if valor_actual:
                parametros.append(valor_actual)
            valor_actual = ""
        elif en_parametros:
            valor_actual += caracter
        print(f"caracter: {caracter}, valor_actual: {valor_actual}")

    if valor_actual:
        parametros.append(valor_actual)

    parametros = parametros[1::2]
    return parametros

if __name__ == "__main__":
    # Ejemplo de uso
    url_ejemplo = "https://retosdeprogramacion.com?year=2023&challenge=0"
    parametros_obtenidos = obtener_parametros_url(url_ejemplo)

    print("Parámetros en la URL:", parametros_obtenidos)