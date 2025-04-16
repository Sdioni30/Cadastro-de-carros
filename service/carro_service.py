from repository.carros_repository import CarrosRepository
from models.carro_dto import Carro_dto
from models.carros import Carro
from sqlalchemy.orm import Session




def criar_carro(carro: Carro_dto, db: Session):
    repo = CarrosRepository(db)
    return repo.save_car(carro)

def inserir_carro(carro: Carro_dto, db: Session):

    novo_carro = Carro(
        nome=carro.nome,
        chassi=carro.chassi,
        ativo=carro.ativo 
        
    )
    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)
    return novo_carro
    
def listar_carro(db: Session):
    repo = CarrosRepository(db)
    return repo.find_all()



def alterar_carro(id: int, carro: Carro_dto, db: Session):
    repo = CarrosRepository(db)
    return repo.alterar_carro(id, carro)



