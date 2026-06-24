import streamlit as st
import google.generativeai as genai
import os

# Configurar la página con diseño moderno
st.set_page_config(page_title="Mi Copilot", page_icon="🤖", layout="centered")

# Título estilizado en la parte superior
st.markdown("<h2 style='text-align: center;'>🤖 Mi Copilot Personalizado</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Tu asistente inteligente de nueva generación</p>", unsafe_allow_html=True)
st.divider()

# Obtener la API Key desde los secretos guardados en Streamlit
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Falta la configuración de seguridad de la API Key. Por favor, revísala en Advanced Settings.")
else:
    # Configurar el modelo de inteligencia artificial
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Crear la memoria del chat si no existe en la sesión actual
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy tu IA personalizada. ¿De qué te gustaría hablar hoy?"}
        ]

    # Mostrar en la pantalla todos los mensajes del historial con su formato profesional
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # El cuadro moderno para escribir la pregunta abajo de la pantalla
    if user_query := st.chat_input("Escribe un mensaje aquí..."):
        
        # Guardar y mostrar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.write(user_query)

        # Generar la respuesta de la IA de forma fluida
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    response = model.generate_content(user_query)
                    answer = response.text
                    st.write(answer)
                    # Guardar la respuesta en el historial
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error("Hubo un pequeño error al conectar con la IA. Inténtalo de nuevo.")
