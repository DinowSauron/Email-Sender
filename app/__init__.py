from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message

#entrar no venv: source venv/Scripts/activate
#pip freeze > requirements.txt
#Instalar os arquivos: pip install -r requirements.txt
#SQL designer

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

#Data Base
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

#precisa existir antes da variavel.
from app.controllers import default