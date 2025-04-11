from fastapi import FastAPI
from http import HTTPStatus
from schemas import Modelo_schemas, CarroUpdate, Carro_excluir


app = FastAPI()

carros = [
    {
        'id': 0,
        'nome': 'Audi TT',
        'chassi' : 'AB123'
    },
    {
        'id': 1,
        'nome': 'Evoque',
        'chassi' : 'AB123'
    },
    {
    'id': 2,
    'nome': 'Golf',
    'chassi' : 'AB123'
    }

]

@app.get('/lista', response_model=list[Modelo_schemas])
def listar_carros():
    for carro in carros:
        print(f'{carro}')
    return carros

@app.post('/lista')
def inserir(carro: Modelo_schemas):
    carros.append(carro.model_dump())
    return carro

@app.put('/alterar_lista/{id}')
def nome(id: int, novo_carro: CarroUpdate):
    for carro in carros:
        if carro['id'] == id:
            carro['nome'] = novo_carro.nome
            return carro


@app.delete('/excluir/{id}')
def retirar_da_lista(id: int, carro: Carro_excluir):
    for carro in carros:
        if carro['id'] == id:
            carros.remove(carro)
            return carro
