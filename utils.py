from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()

def consulta():
    pess = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa)
    print(pessoa.nome)
    print(pessoa.idade)
    for p in pess:
        print(p)
    print(f'Quantidade de pessoas é {len(pess)}')




if __name__ == '__main__':
    insere_pessoas()
    consulta()