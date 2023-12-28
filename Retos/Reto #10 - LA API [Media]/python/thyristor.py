"""
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
"""

import openai

def generar_respuesta_chatgpt(prompt):
    # Reemplaza 'TU_CLAVE_SECRETA' con tu clave de API real de OpenAI.
    openai.api_key = 'TU_CLAVE_SECRETA'

    # Realiza la solicitud a la API de OpenAI (ChatGPT)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    # Obtiene y devuelve la respuesta generada
    respuesta_generada = response.choices[0].text.strip()
    return respuesta_generada

if __name__ == '__main__':
    # Puedes cambiar el prompt según lo que quieras preguntar a ChatGPT
    prompt_usuario = input("Ingresa tu pregunta: ")

    # Realiza la llamada a la API de ChatGPT
    respuesta_chatgpt = generar_respuesta_chatgpt(prompt_usuario)

    # Muestra la respuesta generada por ChatGPT
    print("Respuesta de ChatGPT:")
    print(respuesta_chatgpt)