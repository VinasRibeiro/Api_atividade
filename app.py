from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {'status': 'error', 'mensagem':'Pessoa não encontrada'}
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {'id':pessoa.id, 'nome':pessoa.nome, 'idade':pessoa.idade}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()

        if not pessoa == None:
            pessoa.delete()
            return {'status':'Sucesso', 'mensagem':'pessoa excluida com sucesso'}
        else:
            return {'status':'erro', 'mensagem':'pessoa não encontrada'}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response =[{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        print(atividades)
        return response

    def post(self):
        dados = request.json

        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        if not pessoa == None:
            atividade.save()
            response = {
                'id':atividade.id,
                'nome':atividade.nome,
                'pessoa':atividade.pessoa.nome
            }
            return response
        else:
            return {'status':'erro','mensagem':'Usuario não encontradooooo'}


class Atividade(Resource):
    def delete(self, id):
        ativi = Atividades.query.filter_by(id=id).first()
        if not ativi == None:
            ativi.delete()
            return {'status':'Sucesso', 'mensagem':'Atividade escluida com sucesso'}
        else:
            return{'status':'erro', 'mensagem':'Usuário não encontrado'}

    def put(self, id):
        buscaativ = Atividades.query.filter_by(id=id).first()
        dados = request.json

        print(dados)
        print(buscaativ)

        if not buscaativ == None:
            if 'nome' in dados:
                buscaativ.nome = dados['nome']
                buscaativ.save()
                return 'teste'
        else:
            return 'id não encontrado'



api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(Atividade, '/atividade/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
