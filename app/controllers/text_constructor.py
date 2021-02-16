from datetime import datetime, timezone, timedelta
import os

def GetText(form):
    diference = timedelta(hours=int(os.environ.get("TIMEZONE")))
    data = datetime.now().astimezone(timezone(diference))
    def GetDate():
        return data.strftime("%d/%m/%Y")
    
    def GetHour():
        return data.strftime("%H:%M")
    
    print('[BOT] Gerando Arquivo De Texto...')
    
    return f"""Resumo do cadastro realizado.

Informações:
    Data: {GetDate()}
    Hora: {GetHour()}

Cadastro:
    Nome: {form['name']}
    Email: {form['email']}
    Telefone: {form['tel']}

    País: {form['country']}
    Estado: {form['state']}
    Cidade: {form['city']}
    Logradouro: {form['log']}
    Número: Nº{form['num']}


Assunto: {form['about']}

Mensagem:
 {form['message']}


"""
