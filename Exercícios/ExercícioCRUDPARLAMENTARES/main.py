from flask import Flask, request, jsonify
from datetime import datetime

import json

app = Flask('app')

deputados = []
frentes_parlamentares = []
membros_frentes = []

with open('dataset_deputados.json') as arquivo: 
    data = arquivo.read()
    data_dict = json.loads(data)
    deputados = data_dict['dados']

with open('dataset_frentes.json') as arquivo: 
    data = arquivo.read()
    data_dict = json.loads(data)
    frentes_parlamentares = data_dict['dados']

with open('all_frentes_membros.json') as arquivo: 
    data = arquivo.read()
    data_dict = json.loads(data)
    membros_frentes = data_dict['dados']

@app.route('/deputados', methods=['GET'])
def get_deputados():
    return jsonify(deputados)

@app.route('/deputados', methods=['POST'])
def add_deputado():
    novo_deputado = request.json
    deputados.append(novo_deputado)
    return jsonify({'message': 'Deputado adicionado com sucesso!'})

@app.route('/deputados/<int:id>', methods=['GET'])
def get_deputado_by_id(id):
    for deputado in deputados:
        if deputado['id'] == id:
            return jsonify(deputado)
    return jsonify({'message': 'Deputado não encontrado'})

@app.route('/deputados/<int:id>', methods=['PUT'])
def update_deputado(id):
    for i, deputado in enumerate(deputados):
        if deputado['id'] == id:
            deputados[i] = request.json
            return jsonify({'message': 'Deputado atualizado com sucesso!'})
    return jsonify({'message': 'Deputado não encontrado'})

@app.route('/deputados/<int:id>', methods=['DELETE'])
def delete_deputado(id):
    for i, deputado in enumerate(deputados):
        if deputado['id'] == id:
            del deputados[i]
            return jsonify({'message': 'Deputado removido com sucesso!'})
    return jsonify({'message': 'Deputado não encontrado'})

@app.route('/frentes', methods=['GET'])
def get_frentes_parlamentares():
    return jsonify(frentes_parlamentares)

@app.route('/deputados/nome/<string:nome>', methods=['GET'])
def get_deputado_by_nome(nome):
    result = [dep for dep in deputados if nome.lower() in dep['nome'].lower()]
    return jsonify(result)


@app.route('/frentes/<int:id>/deputados', methods=['GET'])
def get_deputados_by_frente(id):
    deputados_frente = []
    for membro in membros_frentes:
        if membro['frente_id'] == id:
            deputados_frente.append(get_deputado_by_id(membro['deputado_id']))
    return jsonify(deputados_frente)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
