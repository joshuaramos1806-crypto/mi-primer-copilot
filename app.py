import streamlit as stream
from google import genai

# Tu llave que ya sabemos que funciona
mi_llave = "AQ.Ab8RN6KcpBTShHahn8SDbxJ2la1lmWWkRi7AYoYp93ZZyZpKyg"
client = genai.Client(api_key=mi_llave)

# Configuración de la página web
stream.set_page_config(page_title="Mi Copilot Web", page_icon="🤖")
stream.title("🤖 Mi Copilot Personalizado")
stream.write("¡Bienvenido! Hazle cualquier pregunta a tu inteligencia artificial.")

# Cuadro de texto para que el usuario escriba en la web
pregunta = stream.text_input("Escribe tu pregunta aquí:", placeholder="¿En qué te puedo ayudar hoy?")

# Botón para enviar
if stream.button("Preguntar a la IA"):
    if pregunta:
        with stream.spinner("Pensando... 🤔"):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=pregunta,
                )
                # Mostramos la respuesta en una caja bonita
                stream.success("✨ Respuesta de tu IA:")
                stream.write(response.text)
            except Exception as e:
                stream.error(f"Hubo un error: {e}")
    else:
        stream.warning("Por favor, escribe algo primero.")