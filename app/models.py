import enum
from sqlalchemy import Column, Integer, String, Enum, Date, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

# 1. Definimos la tabla Categorias
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True, nullable=False)
    descripcion = Column(String(200), nullable=True)

# 2. Definimos los estados permitidos
class EstadoEquipo(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    ASIGNADO = "ASIGNADO"
    MANTENIMIENTO = "MANTENIMIENTO"
    BAJA = "BAJA"

# 3. Definimos la tabla Equipos (Actualizada con marca/modelo opcionales y descripcion)
class Equipo(Base):
    __tablename__ = "equipos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(100), unique=True, index=True, nullable=False) # Código o Serie
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    marca = Column(String(100), nullable=True)       # Ahora es opcional
    modelo = Column(String(100), nullable=True)      # Ahora es opcional
    descripcion = Column(Text, nullable=True)        # Campo nuevo de descripción
    
    numero_serie = Column(String(100), index=True, nullable=True)
    mac = Column(String(50), nullable=True)

    estado = Column(Enum(EstadoEquipo), default=EstadoEquipo.DISPONIBLE)

    cantidad = Column(Integer, default=1, nullable=False)
    unidad_medida = Column(String(20), default="UND")

    proveedor = Column(String(100), nullable=True)
    fecha_compra = Column(Date, nullable=True)
    garantia = Column(Date, nullable=True)
    ubicacion = Column(String(100), nullable=True)
    observaciones = Column(Text, nullable=True)

    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())

# --- TABLA DE PROVEEDORES ---
class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    empresa = Column(String(100), unique=True, index=True, nullable=False)
    contacto = Column(String(100), nullable=True)
    telefono = Column(String(20), nullable=True)
    correo = Column(String(100), nullable=True)
    direccion = Column(String(200), nullable=True)
    
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())

# Definimos los tipos de movimiento permitidos
class TipoMovimiento(str, enum.Enum):
    ENTREGA = "ENTREGA"
    DEVOLUCION = "DEVOLUCION"
    MANTENIMIENTO = "MANTENIMIENTO"
    BAJA = "BAJA"

# --- TABLA DE MOVIMIENTOS (HISTORIAL) ---
class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    equipo_id = Column(Integer, ForeignKey("equipos.id"), nullable=False)
    
    tipo = Column(Enum(TipoMovimiento), nullable=False)
    responsable = Column(String(100), nullable=False) # Quién se lo lleva o lo recibe
    destino = Column(String(150), nullable=True)      # Cliente, sucursal, torre, etc.
    observaciones = Column(Text, nullable=True)
    
    fecha_movimiento = Column(DateTime(timezone=True), server_default=func.now())