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
