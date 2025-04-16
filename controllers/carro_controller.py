from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.carro_dto import Carro_dto, Car_update_information, Car_public_information, Informations_the_car_for_client
from config.connect_db import get_session
from service.carro_service import list_car, insert_new_car
from repository.carros_repository import CarrosRepository
from models.carros import Carro

router = APIRouter()

#Resolvido
@router.get('/cars', response_model=list[Car_public_information])
def list_car_database(db: Session = Depends(get_session)):
    repo = CarrosRepository(db)
    cars = repo.find_all()
    return cars

@router.post('/new_car_in_system', response_model=Carro_dto)
def insert_car(car: Car_update_information, db: Session = Depends(get_session)):
    new_car = insert_new_car(car, db)
    return new_car


@router.put('/upgrade_car/{id}')
def upgrade_car(id: int, novo_carro: Car_update_information, db: Session = Depends(get_session)):
    repo = CarrosRepository(db)
    car = repo.buscar_carro(id)
    return car


@router.delete('/disable_car/{id}')
def delete_car(id: int, db: Session = Depends(get_session)):
    repo = CarrosRepository(db)
    cars_in_bd = repo.search_the_car_by_id(id)
    
    if not cars_in_bd:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    repo.desativa_carro(cars_in_bd)
        
    return {"Message": "Carro desativado"}


#controller>>repository                         **se não houver logica**
#controller >>> service(logica) >>>repository   **se houver logica**

