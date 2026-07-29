from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/movimientos",
    tags=["Movimientos e Historial"]
)

@router.get("/", response_model=list[schemas.MovimientoResponse])
def listar_movimientos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene el historial completo de movimientos de equipos"""
    return crud.obtener_movimientos(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.MovimientoResponse)
def registrar_movimiento(movimiento: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    """Registra una salida, ingreso o mantenimiento de un equipo"""
    # Validamos primero si el equipo existe
    equipo = crud.obtener_equipo_por_id(db, movimiento.equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="El equipo especificado no existe")
    
    return crud.crear_movimiento(db, movimiento)