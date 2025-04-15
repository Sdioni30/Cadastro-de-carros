from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, registry


table_registry = registry()
@table_registry.mapped_as_dataclass

class Carro:
    __tablename__ = 'carros_padrao'

    id : Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    chassi: Mapped[str] = mapped_column(String, nullable=False)
    
    