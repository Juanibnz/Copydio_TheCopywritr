import tempfile
import os
from google import genai
import time

def copydioPromptCreation(redesSociales, intencionComunica):

    promptCopydio = f"Eres Copydio, un experto en redacción de copys, captions y hashtags para posts de redes sociales como Instagram, LinkedIn, TikTok, emails y difusiones por WhatsApp. Eres el redactor de Startup Grind Bogotá, la comunidad de emprendedores, creadores e innovadores más grande del mundo. Conoces todo el proceso de ideación, investigación en diversas fuentes y redacción, y, mediante la información que te doy, persuades a la audiencia a cumplir el objetivo. Vas a generar 3 posibles opciones de caption y, si son para distintas redes sociales, indicar para cuales. Usa este video como base para escribir el copy de cada red social. Este copy es especificamente para compartir en {redesSociales}. El objetivo de este copy es comunicar {intencionComunica}. No olvides incluir emojis y hashtags relevantes. Máximo 5 hashtags, siempre en minúsculas. Usa un formato de texto sin estilos: Es decir, no uses asteriscos, guiones o elementos de markdown."

    return promptCopydio


def modelExec(content, redesSociales, intencionComunica, api):
    prompt = copydioPromptCreation(redesSociales, intencionComunica)
    client = genai.Client(api)
    print("API Key recibida:", api)  # Verifica que la API Key se reciba correctamente
    print("Contenido recibido:", content)  # Verifica que el contenido se reciba correctamente

    # Create a temporary file to store the uploaded content
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{content.name.split('.')[-1]}") as tmp_file:
        # Write the content to the temporary file
        tmp_file.write(content.getbuffer())
        tmp_file_path = tmp_file.name

    try:
        # Upload the temporary file
        myfile = client.files.upload(file=tmp_file_path)

        while myfile.state.name == "PROCESSING":
            print("El archivo aún se está procesando. Esperando 10 segundos...")
            time.sleep(10)
            myfile = client.files.get(name=myfile.name)

        if myfile.state.name == "FAILED":
            raise ValueError("El procesamiento del archivo falló.")
        
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=[myfile, prompt]
        )

        return response.text

    finally:
        # Clean up the temporary file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)