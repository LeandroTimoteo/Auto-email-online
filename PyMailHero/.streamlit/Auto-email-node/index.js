require("dotenv").config();
const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

const mailOptions = {
  from: process.env.EMAIL_USER,
  to: "destinatario@gmail.com", // altere para o email de destino
  subject: "Teste automático via Node.js",
  text: "Olá! Este é um e-mail enviado automaticamente usando Node.js e nodemailer.",
};

transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.log("Erro ao enviar:", error);
  }
  console.log("✅ Email enviado:", info.response);
});
