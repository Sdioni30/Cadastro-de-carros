from pydantic import BaseModel

class Carro_dto(BaseModel):
    id: int
    name: str
    chassi: str
    status: bool


class CarPublicInformation(BaseModel):
    id: int
    name: str
    status: bool


class Informations_the_car_for_client(BaseModel):
    id: int
    name: str


class Car_update_information_dto(BaseModel):
    name : str


class Chassi_update_information_dto(BaseModel):
    name : str
    chassi : str


class Insert_the_car(BaseModel):
    name: str
    chassi: str
