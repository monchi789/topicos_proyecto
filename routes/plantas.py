from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.plantas import Plantas
from schemas.plantas import PlantaRequest


router = APIRouter(
    tags=['Plantas']
)


@router.get('/plantas/', status_code=status.HTTP_200_OK)
async def get_plantas(db: db_dependency):
    return db.query(Plantas).all()


@router.get('/plantas/{planta_id}', status_code=status.HTTP_200_OK)
async def get_plantas_by_id(db: db_dependency, planta_id: int = Path(gt=0)):
    return db.query(Plantas).filter(Plantas.id == planta_id).first()


@router.post('/plantas', status_code=status.HTTP_201_CREATED)
async def create_plantas(db: db_dependency, planta_request: PlantaRequest):
    
    planta_model = Plantas(**planta_request.model_dump())

    db.add(planta_model)
    db.commit()


@router.put('/plantas/{planta_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_planta(db: db_dependency, planta_request: PlantaRequest, planta_id: int = Path(gt=0)):

    planta_model = db.query(Plantas).filter(Plantas.id == planta_id).first()

    planta_model.nombre_cientifico = planta_request.nombre_cientifico
    planta_model.descripcion = planta_request.descripcion
    planta_model.cuidados = planta_request.cuidados

    db.add(planta_model)
    db.commit()


@router.delete('/plantas/{planta_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_planta(db: db_dependency, planta_id: int = Path(gt=0)):

    db.query(Plantas).filter(Plantas.id == planta_id).delete()
    db.commit()



