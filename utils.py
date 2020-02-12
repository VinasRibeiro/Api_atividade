from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='vinicius', idade=29)
    print(pessoa)

    pessoa.save()

def consulta_pessoas():

    # O metodo query.all() busca todos os registros depois insere eles em uma lista.
    #OBS: Se a quantidade de registros for muito grande, em algum momento isso se torna um problema
    pess = Pessoas.query.all()
    for p in pess:
        print(p.nome,p.idade)

    # Aqui o campo nome já foi indexado na criação no arquivo modelo, isso facilita e reduz gargalos a longo prazo
    # o banco tráz só o necessário para a consulta.
    # No caso ele tráz uma lista que só pdoe ser acessada utilizando um for
    # utilizando o first() ele atribui a pessoa só 1 objeto enão uma lista.
    pessoa = Pessoas.query.filter_by(nome='vinicius').first()
    print(pessoa.nome)
    print(pessoa.idade)
    print(f'Total de registros {len(pess)}')

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='vinicius').first()
    pessoa.idade = 21
    pessoa.save()


def exclui_pessoa():
    try:
        pessoa = Pessoas.query.filter_by(nome='Rafael').first()
        pessoa.delete()
    except:
        if pessoa == None:
            print('Não retornou nada')
        else:
            print('erro desconhecido')






# Este comando verifica se o arquivo esta sendo executado nele mesmo e não chamado em outro lugar
# e executa o comando consulta() ou insere_pessoas()
if __name__ == '__main__':
    #insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()