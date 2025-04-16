from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.carro_dto import Carro_dto, CarroUpdate
from config.connect_db import get_session
from service.carro_service import listar_carro, inserir_carro
from repository.carros_repository import CarrosRepository
from models.carros import Carro

router = APIRouter()


@router.get('/carros', response_model=list[Carro_dto])
def listar_carros_do_bd(db: Session = Depends(get_session)):
    return listar_carro(db)

@router.post('/carros_novos_no_sistema', response_model=Carro_dto)
def insert_car(carro: Carro_dto, db: Session = Depends(get_session)):
    return inserir_carro(carro, db)

@router.put('/alterar_carro/{id}')
def atualizar_carro(id: int, novo_carro: CarroUpdate, db: Session = Depends(get_session)):
    carros = db.query(Carro).all()
    for carro in carros:
        if carro.id == id:
            carro.nome = novo_carro.nome
            carro.chassi = novo_carro.chassi
            db.commit()
            db.refresh(carro)
            return carro
    return {"Mensagem" : "Carro não encontrado"}

@router.delete('/desativar_carro/{id}')
def delete_car(id: int, db: Session = Depends(get_session)):
    repo = CarrosRepository(db)
    carros_no_banco_de_dados = repo.buscar_pelo_id(id)
    
    if not carros_no_banco_de_dados:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    repo.desativa_carro(carros_no_banco_de_dados)
        
    return {"Mensagem": "Carro deletado"}


#controller>>repository                         **se não houver logica**
#controller >>> service(logica) >>>repository   **se houver logica**

