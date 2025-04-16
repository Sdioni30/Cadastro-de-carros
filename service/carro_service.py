from repository.carros_repository import CarrosRepository
from models.carro_dto import Carro_dto
from models.carros import Carro
from sqlalchemy.orm import Session




def create_car(carro: Carro_dto, db: Session):
    repo = CarrosRepository(db)
    return repo.save_car(carro)

def insert_new_car(carro: Carro_dto, db: Session):

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



def upgrade_car(id: int, carro: Carro_dto, db: Session):
    repo = CarrosRepository(db)
    return repo.upgrade_car(id, carro)



