from pydantic import BaseModel

class Carro_dto(BaseModel):
    id: int
    nome: str
    chassi: str
    ativo: bool

class Carro_public_information(BaseModel):
    id: int
    nome: str
    chassi: str
    ativo: bool
    



class CarroUpdate(BaseModel):
    nome : str
    chassi: str
    


    