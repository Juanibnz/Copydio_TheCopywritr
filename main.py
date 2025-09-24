import streamlit as st
import lib.utils as utils

st.title("Copydio - Generador de Copys para Redes Sociales 🧑‍💻")
st.divider()
st.write("Genera copys, captions y hashtags para posts de redes sociales usando IA. Este agente está optimizado para Startup Grind Bogotá. \n Si te gustaría tener esta solución en tu negocio, contáctame 😉.")
st.write("Hecho por [Juan Camilo Ibáñez](https://www.linkedin.com/in/juan-ibanez-patino/).")
st.divider()

with st.form("Infórmale a Copydio 🫡"):
    redesSociales = st.text_input("### Paso 1: ¿En que redes sociales va a estar este copy?")
    intencionComunica = st.text_input("### Paso 2: ¿Qué quieres comunicar?")
    api = st.text_input("### Paso 3: Ingresa tu API Key de Google Gemini (necesario para ejecutar el modelo)", type="password")
    st.markdown("Si no tienes una API Key, obtenla en este [link](https://aistudio.google.com/app/api-keys).")
    files = st.file_uploader("### Paso 4: Sube el contenido base para generar el copy")

    submitted = st.form_submit_button("Generar copys 🚀")

if submitted:
    st.divider()
    
    st.subheader("Aquí están tus copys generados por Copydio:")
    st.text("Esto puede tardar unos minutos ⏳, por favor espera...")
    show_response = utils.modelExec(files, redesSociales, intencionComunica, api)

    if show_response:
        st.text(show_response)