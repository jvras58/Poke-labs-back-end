import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


DATABASE_USER = os.getenv('DATABASE_USER_LOCAL')
DATABASE_SENHA = os.getenv('DATABASE_SENHA_LOCAL')
DATABASE_BANCO = os.getenv('DATABASE_BANCO_LOCAL')
DATABASE_PORT = os.getenv('DATABASE_PORT_LOCAL')
