import streamlit as st
import lib.utils as utils

st.title("Copydio - Generador de Copys para Redes Sociales 🧑‍💻")
st.divider()
st.write("Genera copys, captions y hashtags para posts de redes sociales usando IA.")
st.write("Hecho por [Juan Ibáñez](https://www.linkedin.com/in/juan-ibanez-patino/).")
st.divider()

with st.form("Infórmale a Copydio 🫡"):
    redesSociales = st.text_input("### Paso 1: ¿En que redes sociales va a estar este copy?")
    intencionComunica = st.text_input("### Paso 2: ¿Qué quieres comunicar?")
    files = st.file_uploader("### Paso 3: Sube el contenido base para generar el copy")

    submitted = st.form_submit_button("Generar copys 🚀")

if submitted:
    st.divider()
    
    st.subheader("Aquí están tus copys generados por Copydio:")
    st.text("Esto puede tardar unos minutos ⏳, por favor espera...")
    show_response = utils.modelExec(files, redesSociales, intencionComunica)

    if show_response:
        st.text(show_response)