"""
Funciones para realizar copias de seguridad.
"""

from pathlib import Path
from datetime import datetime
import shutil


ARCHIVO_EXCEL = Path("datos") / "Inventario.xlsx"
CARPETA_RESPALDOS = Path("respaldos")


def crear_respaldo():
    """
    Crea una copia de seguridad del archivo Inventario.xlsx.
    """

    # Verificar que exista el archivo original
    if not ARCHIVO_EXCEL.exists():
        return None

    # Crear la carpeta de respaldos si no existe
    CARPETA_RESPALDOS.mkdir(
        exist_ok=True
    )

    # Obtener fecha y hora actual
    fecha_hora = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    # Crear nombre del respaldo
    nombre_respaldo = (
        f"Inventario_{fecha_hora}.xlsx"
    )

    # Crear ruta completa
    ruta_respaldo = (
        CARPETA_RESPALDOS /
        nombre_respaldo
    )

    # Copiar el archivo
    shutil.copy2(
        ARCHIVO_EXCEL,
        ruta_respaldo
    )

    return ruta_respaldo