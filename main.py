from fastapi import FastAPI
from models.plantas import Base
from config.database import engine
from routes import plantas, prediccion


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(plantas.router)
app.include_router(prediccion.router)