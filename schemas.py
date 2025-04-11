from pydantic import BaseModel

class Modelo_schemas(BaseModel):
    id: int
    nome: str

class CarroUpdate(BaseModel):
    nome : str

class Carro_excluir(BaseModel):
    id: int
    