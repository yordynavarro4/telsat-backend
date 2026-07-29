from sqlalchemy.orm import Session
from app import models, schemas

# --- CRUD PARA CATEGORÍAS ---

def obtener_categorias(db: Session):
    return db.query(models.Categoria).all()

def crear_categoria(db: Session, categoria: schemas.CategoriaCreate):
    nueva = models.Categoria(**categoria.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


# --- CRUD PARA EQUIPOS ---

def obtener_equipos(db: Session, skip: int = 0, limit: int = 100):
    """Busca todos los equipos en la base de datos"""
    return db.query(models.Equipo).offset(skip).limit(limit).all()

def crear_equipo(db: Session, equipo: schemas.EquipoCreate):
    """Guarda un nuevo equipo en la base de datos"""
    db_equipo = models.Equipo(**equipo.model_dump())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

def obtener_equipo_por_id(db: Session, equipo_id: int):
    """Busca un equipo específico usando su ID"""
    return db.query(models.Equipo).filter(models.Equipo.id == equipo_id).first()

def obtener_equipo_por_codigo(db: Session, codigo: str):
    """Busca un equipo específico usando su código interno (Ej: TEL-001)"""
    return db.query(models.Equipo).filter(models.Equipo.codigo == codigo).first()

def actualizar_equipo(db: Session, db_equipo: models.Equipo, equipo_actualizado: schemas.EquipoUpdate):
    """Actualiza los datos de un equipo existente"""
    # Extraemos los datos que sí se enviaron para actualizar (excluimos los nulos)
    datos_nuevos = equipo_actualizado.model_dump(exclude_unset=True)
    
    for clave, valor in datos_nuevos.items():
        setattr(db_equipo, clave, valor)
        
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

def eliminar_equipo(db: Session, db_equipo: models.Equipo):
    """Elimina un equipo de la base de datos"""
    db.delete(db_equipo)
    db.commit()
    return {"mensaje": "Equipo eliminado correctamente"}

# --- CRUD PARA PROVEEDORES ---

def obtener_proveedores(db: Session, skip: int = 0, limit: int = 100):
    """Busca todos los proveedores registrados"""
    return db.query(models.Proveedor).offset(skip).limit(limit).all()

def obtener_proveedor_por_id(db: Session, proveedor_id: int):
    """Busca un proveedor específico por su ID"""
    return db.query(models.Proveedor).filter(models.Proveedor.id == proveedor_id).first()

def crear_proveedor(db: Session, proveedor: schemas.ProveedorCreate):
    """Guarda un nuevo proveedor en la base de datos"""
    db_proveedor = models.Proveedor(**proveedor.model_dump())
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def actualizar_proveedor(db: Session, db_proveedor: models.Proveedor, proveedor_actualizado: schemas.ProveedorUpdate):
    """Actualiza los datos de un proveedor existente"""
    datos_nuevos = proveedor_actualizado.model_dump(exclude_unset=True)
    for clave, valor in datos_nuevos.items():
        setattr(db_proveedor, clave, valor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def eliminar_proveedor(db: Session, db_proveedor: models.Proveedor):
    """Elimina un proveedor de la base de datos"""
    db.delete(db_proveedor)
    db.commit()
    return {"mensaje": "Proveedor eliminado correctamente"}

# --- CRUD PARA MOVIMIENTOS ---

def obtener_movimientos(db: Session, skip: int = 0, limit: int = 100):
    """Obtiene el historial de todos los movimientos"""
    return db.query(models.Movimiento).offset(skip).limit(limit).all()

def crear_movimiento(db: Session, movimiento: schemas.MovimientoCreate):
    """Registra un nuevo movimiento/historial para un equipo"""
    db_movimiento = models.Movimiento(**movimiento.model_dump())
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento