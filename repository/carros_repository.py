from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.carros import Carro
from models.carro_dto import Carro_dto, Car_update_information

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
    
    def alterar_carro(self, carro: Carro_dto, id: int) -> Carro:
        carro_existente = self.session.get(Carro, id)
        if not carro_existente:
            raise HTTPException(status_code=404, detail='O carro não existe')
        for campo, valor in carro.model_dump().items():
            setattr(carro_existente, campo, valor)
        self.session.commit()
        self.session.refresh(carro_existente)
        return carro_existente
    
    def search_the_car_by_id(self, id: int) -> Carro:
        car = self.session.scalar(
            select(Carro).where(Carro.id == id)
        )
        
        return car

    def desativa_carro(self, car: Carro):
        car.status = False
        self.session.commit()
    
    def buscar_carro(self, id: int, car) -> Carro:
        car = self.session.query(Carro).filter(Carro.id == id).first()
        self.session.commit()
        self.session.refresh()
        return car
    
    def update_name_the_car(self, id: int, carro: Car_update_information) -> Carro:
        carro_existente = self.session.get(Carro, id)
        if not carro_existente:
            return 'O carro não existe'
        carro_existente.name = carro.name

        self.session.commit()
        self.session.refresh(carro_existente)
        
        return carro_existente
        
    