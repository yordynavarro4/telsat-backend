from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)


@router.get("/", response_model=list[schemas.CategoriaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)


@router.post("/", response_model=schemas.CategoriaResponse)
def crear(
    categoria: schemas.CategoriaCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_categoria(db, categoria)