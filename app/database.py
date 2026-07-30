import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Obtenemos la URL de la base de datos desde las variables de entorno de Render.
# Si no existe (por ejemplo, si estás probando en tu PC), usará SQLite local.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./inventario_telecom.db")

# Solución para compatibilidad si la URL empieza con "postgres://" en lugar de "postgresql://"
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuramos el engine dependiendo de si es SQLite o PostgreSQL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # Configuración limpia para PostgreSQL (sin el check_same_thread que es exclusivo de SQLite)
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
