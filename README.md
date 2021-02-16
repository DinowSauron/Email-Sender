# Email Sender

uma maneira simples para enviar email com python...


Um exemplo de cadastro via email, onde todos os dados são transmitidos pelo servidor e um email é gerado


Nesse repositório o e-mail retornado irá para o e-mail que você preencheu, o que não é correto, pois o cadastro deve ser com um e-mail da empresa, mas para fins de visualização coloco para enviar o e-mail para o que está listado no formulário .


Veja este repositório rodando agora! sim, preencha o formulário e receberá um email de volta!

Vejá o video [Aqui](https://www.youtube.com/watch?v=eRqlmFnaDe4&feature=youtu.be&ab_channel=LuizClaudio)


Visite o site hospedado na Heroku:
[Veja ele funcionando! Clique aqui](https://email-sender-python.herokuapp.com/) 

<br>

---

## Passos a se seguir... 
* entrar no venv: source venv/Scripts/activate
* Instalar os arquivos: pip install -r requirements.txt
* Gerar os requirimentos, caso mude eles: pip freeze > requirements.txt
* No seu Email.
    * Permitir aplicativos menos seguors.
    * Desabilitar o captcha: https://accounts.google.com/b/0/DisplayUnlockCaptcha
* Colocar o arquivo `.env` com as variaveis de ambiente.
    * MAIL_USERNAME: str
    * MAIL_PASSWORD: str
    * TIMEZONE: int
    * KEY: str (qualquer key, invente uma...)

<br>

Note, enter example values, as they will not be used, the only value of the form that is used in some more dynamic way is the email, as it is necessary to know which inbox to send...
<br>

---

<br>

## Notas:
``` 
Configurações do flask (não utilizadas)

# python app.py runserver  - inicia o server
# python app.py db init    - inicia o database
# python app.py db migrate - faz a migração
# python app.py db upgrade - atualiza a tabela

# entrar no venv: source venv/Scripts/activate
# pip freeze > requirements.txt
# Instalar os arquivos: pip install -r requirements.txt
# SQL designer
# permitir https://accounts.google.com/b/0/DisplayUnlockCaptcha

# https://templates.mailchimp.com/resources/inline-css/
```