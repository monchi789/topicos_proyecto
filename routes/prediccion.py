from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO
from config.database import db_dependency
from models.plantas import Plantas

router = APIRouter()

# Cargar el modelo .h5
model = tf.keras.models.load_model('routes/modelo_1.h5')


async def preprocess_image(file: UploadFile):
    pil_image = Image.open(BytesIO(await file.read()))
    pil_image = pil_image.convert("L")  # Convertir a escala de grises si es necesario
    pil_image = pil_image.resize((250, 250))
    img_array = np.array(pil_image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@router.post("/prediccion")
async def predict_image(db: db_dependency, file: UploadFile):
    try:
        # Preprocesar la imagen
        img_array = await preprocess_image(file)

        # Hacer la predicción
        prediction = model.predict(img_array)
        label = np.argmax(prediction)

        print(label, type(label))

        # Devolver la predicción
        return db.query(Plantas).filter(Plantas.id == int(label)).first()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))