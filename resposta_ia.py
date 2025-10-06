from openai import OpenAI
import streamlit as st

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["openrouter_api_key"],
)

def gerar_resposta(email_texto):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://auto-email-online-jpgtf5i5w9crt2rlgemdaa.streamlit.app",
                "X-Title": "PyMailHero",
            },
            model="openai/gpt-4o",  # ou "mistralai/mistral-7b" se quiser gratuito
            messages=[
                {
                    "role": "user",
                    "content": email_texto
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"
