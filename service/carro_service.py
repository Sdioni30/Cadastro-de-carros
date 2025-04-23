from repository.carros_repository import CarrosRepository
from models.carro_dto import Carro_dto, Car_update_information_dto, Insert_the_car
from models.carros import Carro
from sqlalchemy.orm import Session


def create_car(carro: Carro_dto, db: Session):
    repo = CarrosRepository(db)
    return repo.save_car(carro)


def insert_new_car(carro: Insert_the_car, db: Session):

    novo_carro = Carro(
        name=carro.name,
        chassi=carro.chassi


    )
    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)
    return novo_carro


def list_car(db: Session):
    repo = CarrosRepository(db)
    return repo.find_all()


def change_informations_on_the_car(id: int, carro: Car_update_information_dto, db: Session):
    repo = CarrosRepository(db)
    car_atualized = repo.update_name_and_chassi_car(id, carro)
    return car_atualized


