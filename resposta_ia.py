import streamlit as st
from openai import OpenAI

# Inicializa o cliente OpenAI com OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["openrouter_api_key"],
)

# Função que gera resposta com IA
def gerar_resposta(email_texto):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://auto-email-online-jpgtf5i5w9crt2rlgemdaa.streamlit.app",
                "X-Title": "PyMailHero",
            },
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "user", "content": email_texto}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"

