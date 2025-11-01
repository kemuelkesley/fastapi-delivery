# importando o modelo ou seja o modeles do banco de dados
from models import db
# Criando sessão para definir quantos acessos ao banco de dados pode ter.
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    Session = sessionmaker(bind=db)
    session = Session()

    return session