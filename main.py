from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()

class Usuario(SQLModel):
    nombre: str
    contraseña: str

usuarios = [Usuario(nombre="Josue", contraseña="admin123")]

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API DE Sir_Josue"}

@app.post("/login")
def iniciar_sesion(Login: Usuario):
    for Usuario in usuarios:
        if Usuario.nombre == Login.nombre and Usuario.contraseña == Login.contraseña:
            return {"message": "Inicio de sesión exitoso"}
    return {"message": "Credenciales inválidas"}

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios
