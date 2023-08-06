from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table 
from typing import List
import sqlalchemy as sa


class Base(DeclarativeBase):
    pass

#tabela de assosiação entre pokemon é tipo
pokemon_tipo = Table('pokemon_tipo', 
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id')),
    Column('tipos_id', Integer, ForeignKey('pokemon_tipos.id'))
)
#tabela de assosiação entre pokemon é habilidade 
pokemon_habilidade = Table('pokemon_habilidade',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id')),
    Column('habilidade_id', Integer, ForeignKey('habilidades.id'))
)

class Pokemon(Base):
    __tablename__ = 'pokemon'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    altura = Column(Float)
    peso = Column(Float)
    
    # Relacionamento (m para m) com a tabela de habilidades usando a tabela intermediária
    habilidades = relationship('Habilidade', secondary=pokemon_habilidade, back_populates='pokemon')



class Tipo_Pokemon(Base):
    __tablename__ = 'tipos'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    #relacionamento(m para m) entre pokemon é tipos de pokemon usando a associativa e populando a tabela pokemon com o tipo
    pokemon = relationship("Pokemon", secondary=pokemon_tipo, back_populates="tipo")

    
class Habilidade(Base):
    __tablename__ = 'habilidades'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    descricao = Column(String)

    # Relacionamento (m para m) com a tabela de Pokemon usando a tabela associativa
    pokemon = relationship('Pokemon', secondary=pokemon_habilidade, back_populates='habilidades')







