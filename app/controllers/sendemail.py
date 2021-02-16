# ([('name', 'Luiz Claudio'), ('email', 'luiz.deadzone@gmail.com'), ('tel', '(21) 5555-5555'), ('country', 'Brasil'), 
# ('state', 'RJ'), ('city', 'Rio de Janeiro'), ('log', 'Rua aqui de casa'), ('num', '223'), ('about', 'Minha pesquisa'), 
# ('message', 'aabbcc')]
import os
from flask_mail import Message
from app import mail

def Send(form):
    try:
        print(os.environ.get("MAIL_USERNAME"))
        print(os.environ.get("MAIL_PASSWORD"))
        print(form['email'])
        msg = Message("Hello", sender=os.environ.get("MAIL_USERNAME"), recipients = [form['email']])
        msg.body = "Hello, i'm body!"
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error Detected: {e}")
        return False
        
