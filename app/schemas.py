from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from enum import Enum

# --- ESQUEMAS DE CATEGORÍA ---

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        from_attributes = True


# --- ESQUEMAS DE EQUIPOS ---

class EstadoEquipo(str, Enum):
    DISPONIBLE = "DISPONIBLE"
    ASIGNADO = "ASIGNADO"
    MANTENIMIENTO = "MANTENIMIENTO"
    BAJA = "BAJA"

class EquipoBase(BaseModel):
    codigo: str  # Código o Serie
    categoria_id: int
    marca: Optional[str] = None
    modelo: Optional[str] = None
    descripcion: Optional[str] = None  # <-- Campo nuevo añadido
    numero_serie: Optional[str] = None
    mac: Optional[str] = None
    estado: EstadoEquipo = EstadoEquipo.DISPONIBLE
    cantidad: int = 1
    unidad_medida: str = "UND"
    proveedor: Optional[str] = None
    fecha_compra: Optional[date] = None
    garantia: Optional[date] = None
    ubicacion: Optional[str] = None
    observaciones: Optional[str] = None

class EquipoCreate(EquipoBase):
    pass

class EquipoResponse(EquipoBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True

class EquipoUpdate(BaseModel):
    codigo: Optional[str] = None
    categoria_id: Optional[int] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    descripcion: Optional[str] = None  # <-- Añadido también para las actualizaciones parciales
    numero_serie: Optional[str] = None
    mac: Optional[str] = None
    estado: Optional[EstadoEquipo] = None
    cantidad: Optional[int] = None
    unidad_medida: Optional[str] = None
    proveedor: Optional[str] = None
    fecha_compra: Optional[date] = None
    garantia: Optional[date] = None
    ubicacion: Optional[str] = None
    observaciones: Optional[str] = None


# --- ESQUEMAS DE PROVEEDORES ---

class ProveedorBase(BaseModel):
    empresa: str
    contacto: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorUpdate(BaseModel):
    empresa: Optional[str] = None
    contacto: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None

class ProveedorResponse(ProveedorBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True


# --- ESQUEMAS DE MOVIMIENTOS ---

class TipoMovimientoEnum(str, Enum):
    ENTREGA = "ENTREGA"
    DEVOLUCION = "DEVOLUCION"
    MANTENIMIENTO = "MANTENIMIENTO"
    BAJA = "BAJA"

class MovimientoBase(BaseModel):
    equipo_id: int
    tipo: TipoMovimientoEnum
    responsable: str
    destino: Optional[str] = None
    observaciones: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoResponse(MovimientoBase):
    id: int
    fecha_movimiento: datetime

    class Config:
        from_attributes = True