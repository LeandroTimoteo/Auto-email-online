import streamlit as st
import httpx

def gerar_resposta(email_texto):
    try:
        headers = {
            "Authorization": f"Bearer {st.secrets['openrouter_api_key']}",
            "HTTP-Referer": "https://auto-email-online-jpgtf5i5w9crt2rlgemdaa.streamlit.app",
            "X-Title": "PyMailHero",
        }

        body = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": email_texto}
            ]
        }

        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"


