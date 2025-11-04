# app/main.py
from fastapi import FastAPI
from app.routes import auth
from app.database import engine, Base

# Crear tablas si no existen
Base.metadata.drop_all(bind=engine) 
Base.metadata.create_all(bind=engine)

# Inicializar FastAPI
app = FastAPI(
    title="API de Autenticación",
    version="1.0.0",
    description="API para registro y autenticación de usuarios"
)

# Incluir router de autenticación
app.include_router(auth.router)

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Autenticación"}
