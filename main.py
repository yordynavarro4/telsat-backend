from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import Base, engine, SessionLocal
from app.routers.categorias import router as categorias_router
from app.routers.equipos import router as equipos_router
from app.routers.proveedores import router as proveedores_router
from app.routers.movimientos import router as movimientos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema Inventario TELSAT"
)

# --- CONFIGURACIÓN DE CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite conexiones desde cualquier origen (ideal para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PATCH, DELETE)
    allow_headers=["*"],
)

# --- EVENTO DE INICIO PARA CREAR LAS CATEGORÍAS AUTOMÁTICAMENTE ---
@app.on_event("startup")
def crear_categorias_iniciales():
    db = SessionLocal()
    try:
        query = text("""
            INSERT INTO categorias (id, nombre) VALUES 
            (1, 'ROUTER'), 
            (2, 'BOBINA_FIBRA'), 
            (3, 'BOBINA_COAXIAL'), 
            (4, 'SPLITTER_COAXIAL'), 
            (5, 'SPLITTER_FIBRA'), 
            (6, 'CONECTORES_FIBRA'), 
            (7, 'CONECTORES_COAXIAL'), 
            (8, 'BANDEJA_FUSION'), 
            (9, 'SINTONIZADOR_TV'), 
            (10, 'CORDON_MONOFIBRA'), 
            (11, 'ROSETA'), 
            (12, 'CAJA_NAP'), 
            (13, 'MUFA'), 
            (14, 'HERRAMIENTA'), 
            (15, 'PIGTAIL')
            ON CONFLICT (id) DO NOTHING;
        """)
        db.execute(query)
        db.commit()
    except Exception as e:
        print("Error al insertar categorías automáticas:", e)
        db.rollback()
    finally:
        db.close()

app.include_router(categorias_router)
app.include_router(equipos_router)
app.include_router(proveedores_router)
app.include_router(movimientos_router)

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido al Sistema Inventario TELSAT"
    }
