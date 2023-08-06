from sqlalchemy import create_engine

from constantes import DATABASE_USER, DATABASE_SENHA, DATABASE_BANCO, DATABASE_PORT



class Conexao:
    def __init__(self):
        self.database_user = DATABASE_USER
        self.database_senha = DATABASE_SENHA
        self.database_banco = DATABASE_BANCO
        self.database_port = DATABASE_PORT

    def get_connection_local(self):
        return create_engine(self.get_url_local(), echo=False)

    def get_url_local(self) -> str:
        return f"""postgresql+psycopg2://{self.database_user}:{self.database_senha}@localhost:{self.database_port}/{self.database_banco}"""
