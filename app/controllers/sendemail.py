import os
from flask_mail import Message
from app import mail
from app.controllers.email_constructor import *
from app.controllers.text_constructor import *

def Send(form):
    try:
        print("[BOT] Eniciando Envio De Email...")
        
        msg = Message("Cadastro Realizado Com Sucesso!",
                      sender=os.environ.get("MAIL_USERNAME"),
                      recipients = [form['email']])
        
        msg.html = GetHtml(form)
        msg.attach(f"Cadastro_{(form['name'] + '').replace(' ', '-')}.txt", "txt/text",
                   GetText(form))
        mail.send(msg)
        print('[BOT] Email enviado!')
        return True
    except Exception as e:
        print(f"Error Detected: {e}")
        return False
        
