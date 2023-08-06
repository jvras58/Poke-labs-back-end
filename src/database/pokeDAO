from sqlalchemy.orm import Session
from conexão.conexaoenv import Conexao
from models.dadostestes import pikachu, charmander, bulbasaur, eletrico, fogo, planta, choque_do_trovao, lanca_chamas, raio_solar

conexao = Conexao()
session = Session(bind=conexao.getConnectionLocal())

# envia para o banco

session.add(pikachu)
session.add(charmander)
session.add(bulbasaur)
session.add(eletrico)
session.add(fogo)
session.add(planta)
session.add(choque_do_trovao)
session.add(lanca_chamas)
session.add(raio_solar)


session.commit()
