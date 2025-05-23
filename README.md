# 🚀 CryptoRadar

CryptoRadar é uma aplicação web moderna e segura, desenvolvida com Flask, que integra IA generativa, dados em tempo real e design responsivo para oferecer uma experiência completa no universo das criptomoedas.

---

## 🔍 Problemas que o CryptoRadar resolve

- Falta de dados confiáveis e atualizados sobre criptomoedas, dificultando decisões informadas.  
- Dúvidas técnicas difíceis de esclarecer com segurança e sem aconselhamento financeiro.  
- Riscos de segurança no acesso, proteção de dados e autenticação.  
- Acompanhamento manual do mercado, que é rápido e complexo.  
- Experiência ruim em dispositivos móveis, com interfaces pouco responsivas.  
- Código desorganizado que dificulta manutenção, atualização e expansão.

---

## ⭐ Principais Recursos

- 💰 **Cotações em tempo real:** integração com CoinGecko API para valores atualizados de Bitcoin, Ethereum, Solana e Cardano.  
- 🤖 **Chatbot Gemini AI:** IA com respostas técnicas, sem conselhos financeiros, usando prompt engineering e controle de temperatura.  
- 🔒 **Segurança:** autenticação com Flask-WTF e Bcrypt, proteção CSRF e armazenamento de chaves via `.env`.  
- 🗄️ **Banco de Dados:** SQLAlchemy para CRUD eficiente e seguro.  
- 📱 **Frontend Responsivo:** interface moderna com Bootstrap, CSS customizado e efeitos com Particles.js.  
- 📝 **Formulários com validação:** usando WTForms, com feedback direto ao usuário.  
- 📧 **Inscrição de E-mails:** coleta via AJAX, prevenção de duplicatas e exposição via API REST.  
- ⚙️ **Automação N8n:** envio semanal de e-mails personalizados com atualizações, porcentagens de valorização e curiosidades, programados para domingos ou segundas às 8h.  
- 🧩 **Estrutura Modular:** backend organizado em views, models e helpers para facilitar manutenção e expansão.  
- 🛠️ **Tratamento de exceções:** mensagens amigáveis no console e na interface.  
- 📊 **Logs e monitoramento:** para falhas na IA ou integrações.

---

## 🛠️ Tecnologias Utilizadas

Python | Flask | SQLAlchemy | WTForms | Flask-WTF | Flask-Bcrypt | CoinGecko API | Google Gemini AI | Bootstrap | Particles.js | dotenv | N8n

---

## 📧 Automação de E-mails

O sistema usa N8n para enviar e-mails semanais automáticos com atualizações das principais criptomoedas, porcentagens de valorização e curiosidades do mercado, ajudando os usuários a acompanhar facilmente o mercado.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, abra issues ou pull requests para melhorias e correções.

---

## 🚀 Quer rodar esse projeto na sua máquina?
Esse projeto é um pouquinho diferente… O n8n está rodando dentro de um container Docker na minha máquina, enquanto o backend Flask está rodando direto fora do Docker.
Por conta disso, a configuração envolve detalhes importantes — como o uso de host.docker.internal — que podem variar dependendo de como você pretende rodar aí.

Para facilitar, me manda um e-mail e eu te envio todas as instruções personalizadas, passo a passo, pra você rodar sem complicação!

📩 diogopelinsonduartemoraes@gmail.com


---
## 🔗 Link
Confira o vídeo com a demonstração prática do projeto:

👉 Assista aqui
(link)

🙌 Agradecimento
Muito obrigado por conhecer e usar o CryptoRadar! 🚀
Qualquer dúvida ou sugestão, fique à vontade para entrar em contato.
