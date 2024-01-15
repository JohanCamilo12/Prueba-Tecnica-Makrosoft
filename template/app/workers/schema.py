from pydantic import BaseModel

class WorkerBase(BaseModel):
    nombre: str
    complejidad_acumulada: int
    
class SupportBase(BaseModel):
    descripcion: str
    complejidad: int