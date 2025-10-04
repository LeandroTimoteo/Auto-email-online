import requests
import streamlit as st

def gerar_resposta(email_texto):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['openrouter_api_key']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openchat/openchat-3.5",
        "messages": [
            {"role": "system", "content": "Você é um assistente que responde e-mails de forma educada e profissional."},
            {"role": "user", "content": email_texto}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    resposta = response.json()["choices"][0]["message"]["content"]
    return resposta

