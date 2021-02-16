from app import app

# python run.py runserver  - inicia o server
# python run.py db init    - inicia o database
# python run.py db migrate - faz a migração
# python run.py db upgrade - atualiza a tabela
if __name__ == "__main__":
    app.run()
