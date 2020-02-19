from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


# O parametro check_same_thread False, não verifica se esta na mesma thread.
engine = create_engine('sqlite:///atividades.db', convert_unicode=True,connect_args={'check_same_thread':False})
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__='pessoas'
    #O parâmetro primarykey cria altomaticamente um numero para cada registro novo, tornando unico
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    # O comando commit() finaliza todos os comando que serão executados no banco de dados
    # O comando add adiciona o registro ao banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    # A função backref=backref("children", cascade="all,delete" deleta os registros que possuem chave estrangeira
    # Quando um registro pai é deletado os registro filho dele tbm são
    pessoa = relationship(Pessoas, backref=backref("children", cascade="all,delete"))


    def __repr__(self):
        return f'<Atividades {self.nome}>'

    # O comando commit() finaliza todos os comando que serão executados no banco de dados
    # O comando add adiciona o registro ao banco
    def save(self):
        db_session.add(self)
        db_session.commit()


    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()