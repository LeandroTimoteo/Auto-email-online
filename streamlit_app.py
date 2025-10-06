import streamlit as st
import yagmail
from resposta_ia import gerar_resposta

st.set_page_config(page_title="PyMailHero", page_icon="📧")

st.title("📧 PyMailHero - Automação de Emails")
st.markdown("Escolha abaixo se deseja enviar um e-mail ou gerar uma resposta automática com IA.")

# Navegação lateral
aba = st.sidebar.radio("📌 Função", ["Enviar Email", "Gerar Resposta Automática"])

# Aba 1: Enviar Email Manualmente
if aba == "Enviar Email":
    st.subheader("📤 Enviar Email Manualmente")

    destinatario = st.text_input("✉️ Destinatário (email)")
    assunto = st.text_input("📝 Assunto")
    corpo = st.text_area("💬 Corpo do email")

    if st.button("Enviar Email"):
        if destinatario and assunto and corpo:
            try:
                with st.spinner("Enviando email..."):
                    yag = yagmail.SMTP(user=st.secrets["email"], password=st.secrets["senha"])
                    yag.send(to=destinatario, subject=assunto, contents=corpo)
                st.success("✅ Email enviado com sucesso!")
            except Exception as e:
                st.error(f"❌ Erro ao enviar: {e}")
        else:
            st.warning("⚠️ Preencha todos os campos antes de enviar.")

# Aba 2: Gerar Resposta Automática com IA
elif aba == "Gerar Resposta Automática":
    st.subheader("🤖 Gerador de Resposta com IA")

    email_recebido = st.text_area("📨 Cole aqui o conteúdo do e-mail recebido")
    destinatario_ia = st.text_input("✉️ Destinatário para resposta automática")
    assunto_ia = st.text_input("📝 Assunto da resposta")

    if "resposta_gerada" not in st.session_state:
        st.session_state.resposta_gerada = ""

    if st.button("Gerar Resposta com IA"):
        if email_recebido:
            with st.spinner("Gerando resposta com IA..."):
                resposta = gerar_resposta(email_recebido)
                if resposta.startswith("❌"):
                    st.error(resposta)
                else:
                    st.session_state.resposta_gerada = resposta
                    st.success("✅ Resposta gerada:")
                    st.write(resposta)
        else:
            st.warning("⚠️ Cole o conteúdo do e-mail para gerar uma resposta.")

    if st.session_state.resposta_gerada:
        if st.button("📤 Enviar Resposta por Email"):
            if destinatario_ia and assunto_ia:
                try:
                    with st.spinner("Enviando resposta..."):
                        yag = yagmail.SMTP(user=st.secrets["email"], password=st.secrets["senha"])
                        yag.send(to=destinatario_ia, subject=assunto_ia, contents=st.session_state.resposta_gerada)
                    st.success("✅ Resposta enviada com sucesso!")
                except Exception as e:
                    st.error(f"❌ Erro ao enviar resposta: {e}")
            else:
                st.warning("⚠️ Preencha o destinatário e o assunto para enviar a resposta.")

