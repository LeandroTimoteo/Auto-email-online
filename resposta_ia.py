

import streamlit as st
import httpx

def gerar_resposta(email_texto):
    try:
        # Cabeçalhos exigidos pela OpenRouter
        headers = {
            "Authorization": f"Bearer {st.secrets['openrouter_api_key']}",
            "HTTP-Referer": "https://auto-email-online-jpgtf5i5w9crt2rlgemdaa.streamlit.app",
            "X-Title": "PyMailHero",
        }

        # Prompt estruturado para garantir resposta profissional
        prompt = f"""
Você é um assistente de e-mail profissional. Gere uma resposta educada, clara e objetiva para o seguinte e-mail recebido:

\"\"\"{email_texto}\"\"\"
"""

        # Corpo da requisição
        body = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        # Chamada à API da OpenRouter
        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        response.raise_for_status()

        # Retorna o conteúdo gerado pela IA
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"
