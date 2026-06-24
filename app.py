# Generar respuesta de la IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = model.generate_content(user_query)
                answer = response.text
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error real: {e}") # <-- Esto nos dirá qué está mal
