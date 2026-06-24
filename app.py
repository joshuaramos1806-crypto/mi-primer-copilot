import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Mi Copilot Personalizado", page_icon="🤖", layout="centered")

st.title("🤖 Mi Copilot Personalizado")
st.write("Tu asistente inteligente de nueva generación")

# Conectar con la API usando tus Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy tu IA personalizada. ¿De qué te gustaría hablar hoy?"}
    ]

# Mostrar los mensajes anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Cuadro para escribir
if user_query := st.chat_input("Escribe un mensaje aquí..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    # Generar respuesta de la IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = model.generate_content(user_query)
                answer = response.text
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error("Hubo un pequeño error al conectar con la IA. Inténtalo de nuevo.")
