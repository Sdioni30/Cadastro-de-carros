from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.carro_dto import Carro_dto, CarroUpdate
from config.connect_db import get_session
from service.carro_service import listar_carro, inserir_carro


router = APIRouter()


@router.get('/carros', response_model=list[Carro_dto])
def listar_carros_do_bd(db: Session = Depends(get_session)):
    return listar_carro(db)

@router.post('/carros_novos_no_sistema')
def insert(carro: Carro_dto, db: Session = Depends(get_session)):
    return inserir_carro(carro, db)

@router.put('/alterar_carro/{id}')
def atualizar_carro(id: int, novo_carro: CarroUpdate):
    for carro in Carro_dto:
        if carro['id'] == id:
            carro['nome'] = novo_carro.nome
            return carro
    return {"erro": "Carro não encontrado"}

