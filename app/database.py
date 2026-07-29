from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Datos de conexión
USUARIO = "root"
PASSWORD = "Micasita123!"
HOST = "localhost"
PUERTO = "3306"
BASE_DATOS = "inventario_telecom"

DATABASE_URL = (
    f"mysql+pymysql://{USUARIO}:{PASSWORD}@{HOST}:{PUERTO}/{BASE_DATOS}"
)

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