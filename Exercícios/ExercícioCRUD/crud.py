from flask import Flask, jsonify, request

app = Flask(__name__)
lista = []

def validar_indice(indice):
    if not isinstance(indice, int):
        return False, "O índice deve ser um número inteiro."
    if indice < 0 or indice >= len(lista):
        return False, "O índice está fora dos limites da lista."
    return True, ""

def validar_tipo(valor, tipo_esperado):
    if not isinstance(valor, tipo_esperado):
        return False, f"O valor deve ser do tipo {tipo_esperado.__name__}."
    return True, ""

@app.route('/create', methods=['POST'])
def criar_elemento():
    data = request.get_json()
    if 'elemento' not in data:
        return jsonify({"erro": "O corpo da requisição deve conter a chave 'elemento'."}), 400
    
    lista.append(data['elemento'])
    return jsonify({"mensagem": "Elemento adicionado à lista."})


@app.route('/read', methods=['GET'])
def ler_lista():
    return jsonify({"lista": lista})


@app.route('/read/<int:indice>', methods=['GET'])
def ler_por_indice(indice):
    valido, mensagem = validar_indice(indice)
    if not valido:
        return jsonify({"erro": mensagem}), 400
    
    return jsonify({"elemento": lista[indice]})


@app.route('/read/<string:valor>', methods=['GET'])
def buscar_por_valor(valor):
    if valor in lista:
        return jsonify({"mensagem": f"O valor '{valor}' está presente na lista."})
    else:
        return jsonify({"mensagem": f"O valor '{valor}' não está presente na lista."})


@app.route('/read/duplicates', methods=['GET'])
def verificar_duplicados():
    if len(lista) == len(set(lista)):
        return jsonify({"mensagem": "Não existem elementos duplicados na lista."})
    else:
        return jsonify({"mensagem": "Existem elementos duplicados na lista."})


@app.route('/update/<int:indice>', methods=['PUT'])
def atualizar_elemento(indice):
    data = request.get_json()
    if 'novo_valor' not in data:
        return jsonify({"erro": "O corpo da requisição deve conter a chave 'novo_valor'."}), 400
    
    valido, mensagem_indice = validar_indice(indice)
    if not valido:
        return jsonify({"erro": mensagem_indice}), 400

    valido, mensagem_tipo = validar_tipo(data['novo_valor'], type(lista[indice]))
    if not valido:
        return jsonify({"erro": mensagem_tipo}), 400

    lista[indice] = data['novo_valor']
    return jsonify({"mensagem": f"Elemento na posição {indice} atualizado."})


@app.route('/delete/<int:indice>', methods=['DELETE'])
def deletar_por_indice(indice):
    valido, mensagem = validar_indice(indice)
    if not valido:
        return jsonify({"erro": mensagem}), 400
    
    del lista[indice]
    return jsonify({"mensagem": f"Elemento na posição {indice} excluído."})


@app.route('/delete/<string:valor>', methods=['DELETE'])
def deletar_por_valor(valor):
    if valor not in lista:
        return jsonify({"erro": f"O valor '{valor}' não está presente na lista."}), 400
    
    lista.remove(valor)
    return jsonify({"mensagem": f"Elemento '{valor}' excluído da lista."})


@app.route('/clear', methods=['DELETE'])
def limpar_lista():
    lista.clear()
    return jsonify({"mensagem": "Lista limpa. Todos os elementos foram removidos."})


if __name__ == '__main__':
    app.run(debug=True)
