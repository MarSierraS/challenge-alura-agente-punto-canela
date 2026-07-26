import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------
st.set_page_config(page_title="Agente Punto Canela ☕", page_icon="☕")

st.title("☕ Agente Inteligente - Punto Canela")
st.write(
    "Pregúntame sobre el programa de fidelización de Punto Canela: "
    "cómo funciona, el código QR, los sellos, privacidad de tus datos y más."
)

# ---------------------------------------------------------
# Cargar la base de conocimiento (cachear para que no se
# recargue en cada mensaje del chat)
# ---------------------------------------------------------
@st.cache_resource
def cargar_agente():
    df = pd.read_csv("punto_canela_base_conocimiento.csv")
    vectorizer = TfidfVectorizer()
    matriz_preguntas = vectorizer.fit_transform(df["pregunta"])
    return df, vectorizer, matriz_preguntas

df, vectorizer, matriz_preguntas = cargar_agente()


def responder(pregunta_usuario, umbral_confianza=0.2):
    vector_usuario = vectorizer.transform([pregunta_usuario])
    similitudes = cosine_similarity(vector_usuario, matriz_preguntas)
    indice_mejor = similitudes.argmax()
    score = similitudes[0, indice_mejor]

    if score < umbral_confianza:
        return (
            "Lo siento, no tengo información sobre eso todavía. "
            "¿Puedes reformular tu pregunta sobre el programa de "
            "fidelización de Punto Canela?"
        )
    return df.iloc[indice_mejor]["respuesta"]


# ---------------------------------------------------------
# Historial de chat
# ---------------------------------------------------------
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy el agente de Punto Canela ☕. ¿En qué puedo ayudarte hoy?",
        }
    ]

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

pregunta = st.chat_input("Escribe tu pregunta aquí...")

if pregunta:
    st.session_state.mensajes.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)

    respuesta = responder(pregunta)
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
    with st.chat_message("assistant"):
        st.write(respuesta)
