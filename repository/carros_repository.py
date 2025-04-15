from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.carros import Carro
from models.carro_dto import Carro_dto

class CarrosRepository:  
    def __init__(self, session: Session) -> None:
        self.session = session

    def find_all(self):
        return self.session.scalars(select(Carro)).all()
    

    
    def find_car_by_chassi(self, chassi: str) -> Carro:
        try:
            car = self.session.scalar(
                select(Carro).where(Carro.chassi == chassi)
            )
            return car


        except Exception:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Erro ao acessar banco de dados.',
            )
        
    def inserir_carro_bd(self, carro : Carro):
        return carro
        
    
    def save_car(self, carro: Carro_dto):
        dados = carro.model_dump(exclude={"data"})
        new_car = Carro(**dados)

        self.session.add(new_car)
        self.session.commit()
        return new_car
    
    def alterar_carro(self, jogo: Carro_dto, id: int) -> Carro:
        carro_existente = self.session.get(Carro, id)
        if not carro_existente:
            raise HTTPException(status_code=404, detail='O carro não existe')
        for campo, valor in jogo.model_dump().items():
            setattr(carro_existente, campo, valor)
        self.session.commit()
        self.session.refresh(carro_existente)
        return carro_existente
