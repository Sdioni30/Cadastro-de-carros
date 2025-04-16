from pydantic import BaseModel

class Carro_dto(BaseModel):
    id: int
    name: str
    chassi: str
    status: bool
    
class Car_public_information(BaseModel):
    id: int
    name: str
    status: bool

class Informations_the_car_for_client(BaseModel):
    id: int
    name: str
    
    
class Car_update_information(BaseModel):
    name : str
    chassi: str
    


    