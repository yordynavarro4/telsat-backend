from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- NUEVO

from app.database import Base, engine
from app.routers.categorias import router as categorias_router
from app.routers.equipos import router as equipos_router
from app.routers.proveedores import router as proveedores_router
from app.routers.movimientos import router as movimientos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema Inventario TELSAT"
)

# --- CONFIGURACIÓN DE CORS (NUEVO) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite conexiones desde cualquier origen (ideal para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PATCH, DELETE)
    allow_headers=["*"],
)

app.include_router(categorias_router)
app.include_router(equipos_router)
app.include_router(proveedores_router)
app.include_router(movimientos_router)

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido al Sistema Inventario TELSAT"
    }