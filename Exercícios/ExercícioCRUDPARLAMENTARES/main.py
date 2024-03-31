from flask import Flask, request
from datetime import datetime

import json

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

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

@app.route('/dados/deputados')
def dados_deputados():
  return deputados

@app.route('/dados/frentes')
def dados_frentes_parlamentares():
  return frentes_parlamentares

@app.route('/dados/membros-frentes')
def dados_membros_frentes():
  return membros_frentes

@app.route('/deputado/nome/<string:nome>')
def get_deputado_by_nome(nome):
  deputado = 'NÃO ENCONTRADO'
  for item in deputados:
    if nome in item['nome']:
      deputado = item
  return deputado

app.run(host='0.0.0.0', port=8080)