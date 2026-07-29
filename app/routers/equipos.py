from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

# Creamos el enrutador para Equipos
router = APIRouter(
    prefix="/equipos",
    tags=["Equipos"]
)

@router.get("/", response_model=list[schemas.EquipoResponse])
def listar_equipos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene la lista de todos los equipos registrados"""
    return crud.obtener_equipos(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.EquipoResponse)
def registrar_equipo(equipo: schemas.EquipoCreate, db: Session = Depends(get_db)):
    """Registra un nuevo equipo en el sistema"""
    return crud.crear_equipo(db, equipo)

# --- NUEVAS RUTAS ---

@router.get("/{equipo_id}", response_model=schemas.EquipoResponse)
def buscar_equipo_por_id(equipo_id: int, db: Session = Depends(get_db)):
    """Busca un equipo específico por su ID"""
    equipo = crud.obtener_equipo_por_id(db, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

@router.get("/codigo/{codigo}", response_model=schemas.EquipoResponse)
def buscar_equipo_por_codigo(codigo: str, db: Session = Depends(get_db)):
    """Busca un equipo específico por su código interno (Ej: TEL-001)"""
    equipo = crud.obtener_equipo_por_codigo(db, codigo)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

@router.patch("/{equipo_id}", response_model=schemas.EquipoResponse)
def actualizar_equipo(equipo_id: int, equipo_actualizado: schemas.EquipoUpdate, db: Session = Depends(get_db)):
    """Actualiza uno o varios campos de un equipo existente"""
    equipo_db = crud.obtener_equipo_por_id(db, equipo_id)
    if not equipo_db:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    
    return crud.actualizar_equipo(db, db_equipo=equipo_db, equipo_actualizado=equipo_actualizado)

@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int, db: Session = Depends(get_db)):
    """Elimina un equipo del sistema"""
    equipo_db = crud.obtener_equipo_por_id(db, equipo_id)
    if not equipo_db:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    
    return crud.eliminar_equipo(db, db_equipo=equipo_db)