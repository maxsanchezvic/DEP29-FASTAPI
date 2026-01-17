"""
Hola Mundo - FAST API
"""
from fastapi import FastAPI

app = FastAPI()

#Endpoint para obtener el mensaje de saludo

@app.get("/")
def read_root():
    return {"message":"Hola Mundo"}