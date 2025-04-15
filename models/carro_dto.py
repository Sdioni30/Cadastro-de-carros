from pydantic import BaseModel
#Importar o sqlalchemy

#dados do sqlalchemy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#definição dos modelos de entrada e saída dos dados da API com pydantic
class CarroSchema(BaseModel):
    id: int
    nome: str
    chassi: str


class Modelo_schemas(BaseModel):
    id: int
    nome: str
    chassi: str

class CarroUpdate(BaseModel):
    nome : str


    