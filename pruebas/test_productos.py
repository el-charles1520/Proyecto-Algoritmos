"""
Pruebas unitarias para las funciones de productos.
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
# IMPORTAR FUNCIONES
# ==========================================================

from funciones.productos import (
    agregar_producto,
    listar_productos,
    buscar_producto,
    editar_producto,
    eliminar_producto
)


# ==========================================================
# PRUEBA 1 - LISTAR PRODUCTOS
# ==========================================================

def test_listar_productos():

    productos = listar_productos()

    assert isinstance(
        productos,
        list
    )

    print(
        "✓ test_listar_productos: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - BUSCAR PRODUCTO
# ==========================================================

def test_buscar_producto():

    producto = buscar_producto(
        "Mouse"
    )

    assert producto is not None

    assert producto["nombre"] == "Mouse"

    print(
        "✓ test_buscar_producto: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - AGREGAR PRODUCTO
# ==========================================================

def test_agregar_producto():

    nombre = "ProductoPrueba"

    # Eliminarlo primero si ya existe
    eliminar_producto(
        nombre
    )

    agregar_producto(
        nombre,
        50,
        10
    )

    producto = buscar_producto(
        nombre
    )

    assert producto is not None

    assert producto["precio"] == 50

    assert producto["existencia"] == 10

    print(
        "✓ test_agregar_producto: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - EDITAR PRODUCTO
# ==========================================================

def test_editar_producto():

    resultado = editar_producto(
        "ProductoPrueba",
        "ProductoPruebaEditado",
        75,
        20
    )

    assert resultado is True

    producto = buscar_producto(
        "ProductoPruebaEditado"
    )

    assert producto is not None

    assert producto["precio"] == 75

    assert producto["existencia"] == 20

    print(
        "✓ test_editar_producto: CORRECTA"
    )


# ==========================================================
# PRUEBA 5 - ELIMINAR PRODUCTO
# ==========================================================

def test_eliminar_producto():

    resultado = eliminar_producto(
        "ProductoPruebaEditado"
    )

    assert resultado is True

    producto = buscar_producto(
        "ProductoPruebaEditado"
    )

    assert producto is None

    print(
        "✓ test_eliminar_producto: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - PRODUCTOS")
    print("=" * 55)
    print()

    test_listar_productos()
    test_buscar_producto()
    test_agregar_producto()
    test_editar_producto()
    test_eliminar_producto()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE PRODUCTOS FUERON CORRECTAS")
    print("=" * 55)