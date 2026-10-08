"""
Pruebas unitarias para las funciones de respaldo.
"""

import sys
from pathlib import Path


# ==========================================================
# AGREGAR LA CARPETA PRINCIPAL DEL PROYECTO
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

if str(CARPETA_PROYECTO) not in sys.path:
    sys.path.insert(0, str(CARPETA_PROYECTO))


# ==========================================================
# IMPORTAR FUNCIÓN
# ==========================================================

from funciones.respaldo import crear_respaldo


# ==========================================================
# PRUEBA 1 - CREAR RESPALDO
# ==========================================================

def test_crear_respaldo():

    ruta = crear_respaldo()

    assert ruta is not None

    print(
        "✓ test_crear_respaldo: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - VERIFICAR QUE EL ARCHIVO EXISTA
# ==========================================================

def test_archivo_respaldo():

    ruta = crear_respaldo()

    assert Path(ruta).exists()

    print(
        "✓ test_archivo_respaldo: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - VERIFICAR EXTENSIÓN
# ==========================================================

def test_extension_respaldo():

    ruta = crear_respaldo()

    assert Path(ruta).suffix == ".xlsx"

    print(
        "✓ test_extension_respaldo: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - VERIFICAR NOMBRE DEL ARCHIVO
# ==========================================================

def test_nombre_respaldo():

    ruta = crear_respaldo()

    nombre = Path(ruta).name

    assert nombre.startswith(
        "Inventario_"
    )

    assert nombre.endswith(
        ".xlsx"
    )

    print(
        "✓ test_nombre_respaldo: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - RESPALDO")
    print("=" * 55)
    print()

    test_crear_respaldo()
    test_archivo_respaldo()
    test_extension_respaldo()
    test_nombre_respaldo()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE RESPALDO FUERON CORRECTAS")
    print("=" * 55)