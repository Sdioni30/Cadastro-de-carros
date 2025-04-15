from repository.carros_repository import CarrosRepository
from models.carro_dto import CarroSchema
from sqlalchemy.orm import Session

def criar_carro(carro: CarroSchema, db: Session):
    repo = CarrosRepository(db)
    return repo.save_car(carro)


def listar_carro(db: Session):
    repo = CarrosRepository(db)
    return repo.find_all()

def encontrar_por_chassi(chassi: str, db: Session):
    repo = CarrosRepository(db)
    return repo.find_car_by_chassi(chassi)

def alterar_carro(id: int, carro: CarroSchema, db: Session):
    repo = CarrosRepository(db)
    return repo.alterar_carro(id, carro)
