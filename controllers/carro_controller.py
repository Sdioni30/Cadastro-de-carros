from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.carro_dto import CarroSchema, CarroUpdate, Modelo_schemas
from models.carro_dto import CarroSchema
from config.connect_db import get_session
from service.carro_service import listar_carro


router = APIRouter()


@router.get('/carros', response_model=list[Modelo_schemas])
def listar_carros_do_bd(db: Session = Depends(get_session)):
    return listar_carro(db)

@router.post('/carros')
def inserir(carro: Modelo_schemas, db: Session = Depends(get_session)):
    carro.append(carro.model_dump())
    return carro

@router.put('/alterar_carro/{id}')
def atualizar_carro(id: int, novo_carro: CarroUpdate):
    for carro in CarroSchema:
        if carro['id'] == id:
            carro['nome'] = novo_carro.nome
            return carro
    return {"erro": "Carro não encontrado"}

