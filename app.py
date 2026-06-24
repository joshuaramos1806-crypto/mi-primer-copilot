import streamlit as st
import google.generativeai as genai

# 1. Configuración de la ventana
st.set_page_config(page_title="Mi Copilot", page_icon="🤖", layout="centered")
st.title("🤖 Mi Copilot Personalizado")
st.write("Tu asistente inteligente reiniciado desde cero")

# 2. Conectar la API Key usando los Secrets de Streamlit
api_key_segura = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key_segura)

# 3. Configurar el modelo correcto
model = genai.GenerativeModel("gemini-1.5-flash")

# 4. Crear el almacén de mensajes (Historial)
if "historial" not in st.session_state:
    st.session_state.historial = [
        {"role": "assistant", "content": "¡Hola de nuevo! Hemos reiniciado el sistema con éxito. ¿De qué deseas hablar?"}
    ]

# 5. Mostrar los mensajes en la pantalla
for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

# 6. Cuadro de texto para que escribas
if pregunta_usuario := st.chat_input("Escribe tu mensaje aquí..."):
    
    # Mostrar lo que tú escribiste
    st.session_state.historial.append({"role": "user", "content": pregunta_usuario})
    with st.chat_message("user"):
        st.write(pregunta_usuario)

    # Pedirle la respuesta a la IA de Google
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = model.generate_content(pregunta_usuario)
                texto_ia = response.text
                st.write(texto_ia)
                st.session_state.historial.append({"role": "assistant", "content": texto_ia})
            except Exception as error_detectado:
                st.error(f"Aviso del sistema: {error_detectado}")
