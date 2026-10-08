"""
Pruebas unitarias para las funciones de clientes.
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

from funciones.clientes import (
    agregar_cliente,
    listar_clientes,
    buscar_cliente,
    editar_cliente,
    eliminar_cliente
)


# ==========================================================
# PRUEBA 1 - LISTAR CLIENTES
# ==========================================================

def test_listar_clientes():

    clientes = listar_clientes()

    assert isinstance(
        clientes,
        list
    )

    print(
        "✓ test_listar_clientes: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - BUSCAR CLIENTE
# ==========================================================

def test_buscar_cliente():

    cliente = buscar_cliente(
        "Juan Pérez"
    )

    assert cliente is not None

    assert cliente["nombre"] == "Juan Pérez"

    print(
        "✓ test_buscar_cliente: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - AGREGAR CLIENTE
# ==========================================================

def test_agregar_cliente():

    nombre = "ClientePrueba"

    # Eliminarlo primero si ya existe
    eliminar_cliente(
        nombre
    )

    agregar_cliente(
        nombre,
        "000000-0",
        "Dirección de prueba"
    )

    cliente = buscar_cliente(
        nombre
    )

    assert cliente is not None

    assert cliente["nit"] == "000000-0"

    assert cliente["direccion"] == "Dirección de prueba"

    print(
        "✓ test_agregar_cliente: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - EDITAR CLIENTE
# ==========================================================

def test_editar_cliente():

    resultado = editar_cliente(
        "ClientePrueba",
        "ClientePruebaEditado",
        "111111-1",
        "Nueva dirección"
    )

    assert resultado is True

    cliente = buscar_cliente(
        "ClientePruebaEditado"
    )

    assert cliente is not None

    assert cliente["nit"] == "111111-1"

    assert cliente["direccion"] == "Nueva dirección"

    print(
        "✓ test_editar_cliente: CORRECTA"
    )


# ==========================================================
# PRUEBA 5 - ELIMINAR CLIENTE
# ==========================================================

def test_eliminar_cliente():

    resultado = eliminar_cliente(
        "ClientePruebaEditado"
    )

    assert resultado is True

    cliente = buscar_cliente(
        "ClientePruebaEditado"
    )

    assert cliente is None

    print(
        "✓ test_eliminar_cliente: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - CLIENTES")
    print("=" * 55)
    print()

    test_listar_clientes()
    test_buscar_cliente()
    test_agregar_cliente()
    test_editar_cliente()
    test_eliminar_cliente()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE CLIENTES FUERON CORRECTAS")
    print("=" * 55)