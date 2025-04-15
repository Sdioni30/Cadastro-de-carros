from pydantic import BaseModel

class Carro_dto(BaseModel):
    id: int
    nome: str
    chassi: str


'''class Modelo_schemas(BaseModel):
    id: int
    nome: str
    chassi: str
'''

class CarroUpdate(BaseModel):
    nome : str


    