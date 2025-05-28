import streamlit as st
# Columnas con imagenes
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Calendario
import streamlit as st
import datetime

st.title("Ejemplo de fecha")

# Widget: date_input
fecha = st.date_input("Selecciona una fecha", value=datetime.date.today())

st.write("La fecha seleccionada es:", fecha)
# mini bot
import streamlit as st

st.set_page_config(page_title="Ejemplo Chat", layout="centered")

st.title("💬 Mini Chatbot (solo repite lo que dices)")

# Entrada tipo chat (abajo de la pantalla)
user_input = st.chat_input("Escribe algo...")

# Si el usuario escribe algo, mostramos los mensajes
if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user").write(user_input)

    # Mostrar una respuesta simple del asistente
    st.chat_message("assistant").write(f"{user_input} <- eso dijiste")

