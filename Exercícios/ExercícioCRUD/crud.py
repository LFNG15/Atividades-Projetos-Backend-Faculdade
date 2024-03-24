from flask import Flask, jsonify, request

app = Flask(__name__)

lista = []

@app.route('/lista/create', methods=['POST'])
def add():
    if 'valor' not in request.form:
        return jsonify({'message': 'Erro: Parâmetro "valor" ausente'}), 400
    
    valor = request.form['valor']
    lista.append(valor)
    return jsonify({'message': f'Elemento "{valor}" adicionado à lista', 'lista': lista}), 200

@app.route('/lista/read', methods=['GET'])
def get_lista():
    return jsonify({'lista': lista}), 200

@app.route('/lista/read/<int:indice>', methods=['GET'])
def get_elemento_por_indice(indice):
    if indice < 0 or indice >= len(lista):
        return jsonify({'message': f'Erro: Índice {indice} fora do intervalo da lista'}), 400
    
    return jsonify({'elemento': lista[indice]}), 200

@app.route('/lista/read/<string:valor>', methods=['GET'])
def get_elemento_por_valor(valor):
    if valor not in lista:
        return jsonify({'message': f'Erro: Elemento "{valor}" não encontrado na lista'}), 404
    
    return jsonify({'indice': lista.index(valor)}), 200

@app.route('/lista/check/<string:valor>', methods=['GET'])
def check_elemento(valor):
    return jsonify({'presente': valor in lista}), 200

@app.route('/lista/check_duplicates', methods=['GET'])
def check_duplicates():
    duplicates = set([x for x in lista if lista.count(x) > 1])
    return jsonify({'duplicates': list(duplicates)}), 200

@app.route('/lista/update/<int:indice>', methods=['PUT'])
def update_elemento(indice):
    if indice < 0 or indice >= len(lista):
        return jsonify({'message': f'Erro: Índice {indice} fora do intervalo da lista'}), 400
    
    novo_valor = request.form.get('novo_valor')
    if not novo_valor:
        return jsonify({'message': 'Erro: Parâmetro "novo_valor" ausente'}), 400
    
    lista[indice] = novo_valor
    return jsonify({'message': f'Elemento no índice {indice} atualizado para "{novo_valor}"', 'lista': lista}), 200

@app.route('/lista/delete/<int:indice>', methods=['DELETE'])
def delete_elemento_por_indice(indice):
    if indice < 0 or indice >= len(lista):
        return jsonify({'message': f'Erro: Índice {indice} fora do intervalo da lista'}), 400
    
    deleted_element = lista.pop(indice)
    return jsonify({'message': f'Elemento "{deleted_element}" removido da lista', 'lista': lista}), 200

@app.route('/lista/delete/<string:valor>', methods=['DELETE'])
def delete_elemento_por_valor(valor):
    if valor not in lista:
        return jsonify({'message': f'Erro: Elemento "{valor}" não encontrado na lista'}), 404
    
    lista.remove(valor)
    return jsonify({'message': f'Elemento "{valor}" removido da lista', 'lista': lista}), 200

@app.route('/lista/clear', methods=['DELETE'])
def clear_lista():
    lista.clear()
    return jsonify({'message': 'Lista limpa', 'lista': lista}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
