"""
Pruebas unitarias para las funciones de pedidos.
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

from funciones.pedidos import (
    agregar_pedido,
    listar_pedidos,
    buscar_pedidos_cliente,
    eliminar_pedido
)


# ==========================================================
# PRUEBA 1 - LISTAR PEDIDOS
# ==========================================================

def test_listar_pedidos():

    pedidos = listar_pedidos()

    assert isinstance(
        pedidos,
        list
    )

    print(
        "✓ test_listar_pedidos: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - BUSCAR PEDIDOS POR CLIENTE
# ==========================================================

def test_buscar_pedidos_cliente():

    pedidos = buscar_pedidos_cliente(
        "Juan Pérez"
    )

    assert isinstance(
        pedidos,
        list
    )

    print(
        "✓ test_buscar_pedidos_cliente: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - AGREGAR PEDIDO
# ==========================================================

def test_agregar_pedido():

    # Eliminar primero el pedido de prueba
    eliminar_pedido(
        "ClientePrueba",
        "Mouse"
    )

    resultado = agregar_pedido(
        "ClientePrueba",
        "Mouse",
        3
    )

    assert resultado is True

    pedidos = buscar_pedidos_cliente(
        "ClientePrueba"
    )

    assert len(pedidos) >= 1

    pedido = pedidos[-1]

    assert pedido["producto"] == "Mouse"

    assert pedido["cantidad"] == 3

    print(
        "✓ test_agregar_pedido: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - VERIFICAR CÁLCULO DEL VALOR
# ==========================================================

def test_calcular_valor_pedido():

    pedidos = buscar_pedidos_cliente(
        "ClientePrueba"
    )

    assert len(pedidos) >= 1

    pedido = pedidos[-1]

    # Mouse = Q100
    # Cantidad = 3
    # Valor esperado = Q300

    assert pedido["valor"] == 300

    print(
        "✓ test_calcular_valor_pedido: CORRECTA"
    )


# ==========================================================
# PRUEBA 5 - ELIMINAR PEDIDO
# ==========================================================

def test_eliminar_pedido():

    resultado = eliminar_pedido(
        "ClientePrueba",
        "Mouse"
    )

    assert resultado is True

    pedidos = buscar_pedidos_cliente(
        "ClientePrueba"
    )

    assert len(pedidos) == 0

    print(
        "✓ test_eliminar_pedido: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - PEDIDOS")
    print("=" * 55)
    print()

    test_listar_pedidos()
    test_buscar_pedidos_cliente()
    test_agregar_pedido()
    test_calcular_valor_pedido()
    test_eliminar_pedido()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE PEDIDOS FUERON CORRECTAS")
    print("=" * 55)