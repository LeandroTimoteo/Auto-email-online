from openai import OpenAI

# Inicializa o cliente com a nova chave e URL da OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# Faz a requisição de completions com IA
completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "https://auto-email-online-jpgtf5i5w9crt2rlgemdaa.streamlit.app",  # URL do seu app
        "X-Title": "PyMailHero",  # Nome do projeto
    },
    model="mistralai/mistral-7b-instruct",  # ✅ modelo gratuito e válido
    messages=[
        {
            "role": "user",
            "content": "Olá, tudo bem? Me diga algo sobre inteligência artificial."
        }
    ]
)

# Exibe a resposta gerada pela IA
print("✅ Resposta da IA:")
print(completion.choices[0].message.content)

