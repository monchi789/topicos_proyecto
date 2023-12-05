from pydantic import BaseModel, Field
from typing import Optional


class PlantaRequest(BaseModel):

    nombre_cientifico: str 
    descripcion: str
    cuidados: str

    class Config:
        json_schema_extra = {
            'example': {
                'nombre_cientifico': 'Ruta graveolens',
                'descripcion': 'Es un arbusto perenne de hasta 1 metro de altura. Sus hojas son de color verde brillante y tienen un aroma aromático. Es una planta resistente a la sequía y al frío.', 
                'cuidados': 'Regar regularmente, especialmente durante los meses de verano.'

            }
        }