from flask import request
from flask_restful import Resource
import json


lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        global lista_habilidades
        lista_habilidades = json.loads(request.data)
        return lista_habilidades


class InserirAlterarHabilidade(Resource):
    def get(self, id):
        return lista_habilidades[id]

    def put(self, id):
        lista_habilidades[id] = json.loads(request.data)
        return lista_habilidades[id]

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'Status': 'Sucesso', 'Mensagem': 'Registro deletado com sucesso'}
