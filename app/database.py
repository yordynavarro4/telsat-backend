from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambiamos a SQLite para que funcione directamente en la nube sin configuraciones extra
DATABASE_URL = "sqlite:///./inventario_telecom.db"

# engine con configuración especial para SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

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
