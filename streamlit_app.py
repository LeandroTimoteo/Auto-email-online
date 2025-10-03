import streamlit as st
import yagmail

st.set_page_config(page_title="PyMailHero", page_icon="📧")

st.title("📧 PyMailHero - Automação de Emails")
st.markdown("Preencha os campos abaixo para enviar um e-mail automaticamente.")

# Campos do formulário
destinatario = st.text_input("✉️ Destinatário (email)")
assunto = st.text_input("📝 Assunto")
corpo = st.text_area("💬 Corpo do email")

# Botão de envio
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