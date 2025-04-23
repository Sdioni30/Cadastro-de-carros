from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.carro_dto import Carro_dto, CarPublicInformation, Insert_the_car, Chassi_update_information_dto
from config.connect_db import get_session
from service.carro_service import insert_new_car, change_informations_on_the_car
from repository.carros_repository import CarrosRepository


router = APIRouter()


@router.get('/cars', response_model=list[CarPublicInformation])
def list_car_database_for_client(db: Session = Depends(get_session)):
    list_information: list[CarPublicInformation] = []
    repo = CarrosRepository(db)
    cars = repo.find_all()
    
    for car in cars:
        data = CarPublicInformation (
            id=car.id,
            name=car.name,
            status=car.status
        )
        list_information.append(data)

    return list_information


@router.post('/new_car_in_system', response_model=Carro_dto)
def insert_car(car: Insert_the_car, db: Session = Depends(get_session)):
    new_car = insert_new_car(car, db)
    return new_car


@router.put('/upgrade_car/{id}')
def update_car(id: int, car: Chassi_update_information_dto, db: Session = Depends(get_session)):
    carro = change_informations_on_the_car(id, car, db)
    # transformar entidade carro em um dto
    return Chassi_update_information_dto(name=carro.name, chassi=carro.chassi)


@router.put('/check_chassi/')
def check_chassi(chassi : str,db: Session = Depends(get_session) ):
    repo = CarrosRepository(db)
    matching_all_cars = repo.find_car_chassi(chassi)
    if not matching_all_cars:
        return {'Message' : 'Chassi não cadastrado ❌'}
    if len(matching_all_cars)>1:
        return {
            'ALERT': 'Chassi clonado ❌',
            'Carros': matching_all_cars
        }
    return {'Chassi OK ✅': matching_all_cars[0]}


@router.delete('/disable_car/{id}')
def delete_car(id: int, db: Session = Depends(get_session)):
    repo = CarrosRepository(db)
    cars_in_bd = repo.search_car_by_id(id)
    
    if not cars_in_bd:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    repo.desativa_carro(cars_in_bd)
        
    return {"Message": "Carro desativado"}


#controller>>repository                         **se não houver logica**
#controller >>> service(logica) >>>repository   **se houver logica**

