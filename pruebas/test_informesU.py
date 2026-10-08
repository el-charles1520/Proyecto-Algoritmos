"""
Pruebas unitarias para las funciones de informes.
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

from funciones.informes import (
    obtener_informe_productos,
    obtener_informe_clientes,
    obtener_informe_pedidos,
    calcular_total_ventas,
    contar_productos,
    contar_clientes,
    contar_pedidos
)


# ==========================================================
# PRUEBA 1 - INFORME DE PRODUCTOS
# ==========================================================

def test_informe_productos():

    productos = obtener_informe_productos()

    assert isinstance(
        productos,
        list
    )

    assert len(productos) > 0

    print(
        "✓ test_informe_productos: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - INFORME DE CLIENTES
# ==========================================================

def test_informe_clientes():

    clientes = obtener_informe_clientes()

    assert isinstance(
        clientes,
        list
    )

    assert len(clientes) > 0

    print(
        "✓ test_informe_clientes: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - INFORME DE PEDIDOS
# ==========================================================

def test_informe_pedidos():

    pedidos = obtener_informe_pedidos()

    assert isinstance(
        pedidos,
        list
    )

    assert len(pedidos) > 0

    print(
        "✓ test_informe_pedidos: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - TOTAL DE VENTAS
# ==========================================================

def test_total_ventas():

    total = calcular_total_ventas()

    assert isinstance(
        total,
        (int, float)
    )

    assert total >= 0

    print(
        "✓ test_total_ventas: CORRECTA"
    )


# ==========================================================
# PRUEBA 5 - CONTAR PRODUCTOS
# ==========================================================

def test_contar_productos():

    cantidad = contar_productos()

    assert isinstance(
        cantidad,
        int
    )

    assert cantidad > 0

    print(
        "✓ test_contar_productos: CORRECTA"
    )


# ==========================================================
# PRUEBA 6 - CONTAR CLIENTES
# ==========================================================

def test_contar_clientes():

    cantidad = contar_clientes()

    assert isinstance(
        cantidad,
        int
    )

    assert cantidad > 0

    print(
        "✓ test_contar_clientes: CORRECTA"
    )


# ==========================================================
# PRUEBA 7 - CONTAR PEDIDOS
# ==========================================================

def test_contar_pedidos():

    cantidad = contar_pedidos()

    assert isinstance(
        cantidad,
        int
    )

    assert cantidad > 0

    print(
        "✓ test_contar_pedidos: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - INFORMES")
    print("=" * 55)
    print()

    test_informe_productos()
    test_informe_clientes()
    test_informe_pedidos()
    test_total_ventas()
    test_contar_productos()
    test_contar_clientes()
    test_contar_pedidos()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE INFORMES FUERON CORRECTAS")
    print("=" * 55)