from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

@router.get("/", response_model=list[schemas.ProveedorResponse])
def listar_proveedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene la lista de todos los proveedores registrados"""
    return crud.obtener_proveedores(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.ProveedorResponse)
def registrar_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    """Registra un nuevo proveedor en el sistema"""
    return crud.crear_proveedor(db, proveedor)

@router.get("/{proveedor_id}", response_model=schemas.ProveedorResponse)
def buscar_proveedor_por_id(proveedor_id: int, db: Session = Depends(get_db)):
    """Busca un proveedor específico por su ID"""
    proveedor = crud.obtener_proveedor_por_id(db, proveedor_id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

@router.patch("/{proveedor_id}", response_model=schemas.ProveedorResponse)
def actualizar_proveedor(proveedor_id: int, proveedor_actualizado: schemas.ProveedorUpdate, db: Session = Depends(get_db)):
    """Actualiza los datos de un proveedor existente"""
    proveedor_db = crud.obtener_proveedor_por_id(db, proveedor_id)
    if not proveedor_db:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return crud.actualizar_proveedor(db, db_proveedor=proveedor_db, proveedor_actualizado=proveedor_actualizado)

@router.delete("/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Elimina un proveedor del sistema"""
    proveedor_db = crud.obtener_proveedor_por_id(db, proveedor_id)
    if not proveedor_db:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return crud.eliminar_proveedor(db, db_proveedor=proveedor_db)