📧 PyMailHero – Auto-email-online
PyMailHero é uma aplicação web inteligente desenvolvida com Streamlit e Yagmail que automatiza o envio e a resposta de e-mails com suporte à inteligência artificial. Ideal para profissionais que desejam agilidade, elegância e eficiência na comunicação por e-mail.

🚀 Funcionalidades
📤 Envio manual de e-mails com autenticação segura via Gmail

🤖 Geração automática de respostas com IA usando modelos da OpenRouter

✅ Feedback visual em tempo real para sucesso ou erro

🔐 Gerenciamento seguro de credenciais com st.secrets

☁️ Pronto para deploy no Streamlit Cloud

🧠 Inteligência Artificial
A resposta automática é gerada via OpenRouter, utilizando o modelo mistralai/mistral-7b-instruct, com integração via httpx. O prompt é cuidadosamente estruturado para garantir respostas profissionais, educadas e claras.

🛠️ Tecnologias Utilizadas
Tecnologia	Finalidade
Python	Lógica principal do app
Streamlit	Interface web interativa
Yagmail	Envio de e-mails via SMTP Gmail
httpx	Integração com API da OpenRouter
Gmail SMTP	Autenticação e envio seguro
📦 Instalação Local
bash
git clone https://github.com/LeandroTimoteo/Auto-email-online.git
cd Auto-email-online
pip install -r requirements.txt
streamlit run streamlit_app.py
🔐 Configuração de Secrets (Streamlit Cloud)
No painel de Secrets do Streamlit Cloud, adicione:

toml
email = "seu-email@gmail.com"
senha = "sua-senha-de-aplicativo"
openrouter_api_key = "sua-chave-openrouter"
⚠️ Use uma senha de aplicativo do Gmail para segurança.

💡 Exemplos de Uso
✉️ Envio manual:
Preencha destinatário, assunto e corpo

Clique em Enviar Email

🤖 Resposta automática:
Cole o e-mail recebido

Clique em Gerar Resposta com IA

Revise e envie com um clique

🖼️ Interface do PyMailHero
📤 Tela de Envio de Email

🤖 Tela de Geração de Resposta com IA

🖼️ Visual Completo do App

🧪 Testado em
✅ Streamlit Cloud

✅ Gmail com autenticação de dois fatores

📬 Contato
Desenvolvido por Analista de Sistemas: Leandro Timóteo Silva

📧 E-mail: leandrinhots6@gmail.com

💼 LinkedIn: linkedin.com/in/leandro-timóteo-ads

📱 WhatsApp: Enviar mensagem