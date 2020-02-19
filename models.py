#classes que irão referenciar as tabelas

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship #são responsaveis por criar a sessão
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property() #serve para criar e trabalhar com o db

class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True) #deixa a columa mais rápida na busca
    idade = Column(Integer)
    
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")
    
def init_db():
    Base.metadata.create_all(bind=engine)