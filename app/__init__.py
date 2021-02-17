from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object('config')

# DataBase
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command("db", MigrateCommand)

mail = Mail(app)

#precisa existir antes da variavel.
from app.controllers import default