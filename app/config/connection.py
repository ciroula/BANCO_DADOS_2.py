from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parametros de conexao com MySQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# URL de conexao para BD MySQL.
#DATABASE_URL =  f"mysql+pymysql://usuario:senha@host:porta/nome_bd"
DATABASE_URL =  f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#conectando ao baco de dados
db = create_engine(DATABASE_URL)
Session = sessionmaker (bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session() #Criar uma sessao para acoes no BD.
    try:
        yield db # Caso a sessao realize todas as tarefas, salva a operacao. 
        db.commit()
    except Exception as erro:
        db.rollback() # Desfaz todas as alteracoes em caso de erro em alguma operacao.
        raise erro # Lança um excecao
    finally:
        db.close() # Fecha sessao com BD.