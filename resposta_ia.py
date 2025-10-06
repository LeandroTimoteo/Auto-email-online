from openai import OpenAI

# Inicializa o cliente OpenRouter via SDK compatível com OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# Função que gera resposta automática com IA
def gerar_resposta(email_texto):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://pymailhero.streamlit.app",  # opcional para ranking
                "X-Title": "PyMailHero",  # opcional para ranking
            },
            model="mistralai/mistral-7b-instruct:free",  # ✅ modelo gratuito
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
