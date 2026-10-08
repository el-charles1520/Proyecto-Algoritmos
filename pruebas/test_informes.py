"""
Prueba del módulo de informes.
"""

import sys
from pathlib import Path


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CARPETA_PROYECTO))


from funciones.informes import (
    obtener_informe_productos,
    obtener_informe_clientes,
    obtener_informe_pedidos,
    calcular_total_ventas,
    contar_productos,
    contar_clientes,
    contar_pedidos
)


print()
print("==========================================")
print("PRUEBA DEL MÓDULO DE INFORMES")
print("==========================================")


# ==========================================================
# INFORME DE PRODUCTOS
# ==========================================================

print()
print("1. INFORME DE PRODUCTOS")
print("------------------------------------------")

productos = obtener_informe_productos()

for producto in productos:

    print(
        f"Producto: {producto['nombre']} | "
        f"Precio: Q{producto['precio']} | "
        f"Existencia: {producto['existencia']}"
    )


# ==========================================================
# INFORME DE CLIENTES
# ==========================================================

print()
print("2. INFORME DE CLIENTES")
print("------------------------------------------")

clientes = obtener_informe_clientes()

for cliente in clientes:

    print(
        f"Cliente: {cliente['nombre']} | "
        f"NIT: {cliente['nit']} | "
        f"Dirección: {cliente['direccion']}"
    )


# ==========================================================
# INFORME DE PEDIDOS
# ==========================================================

print()
print("3. INFORME DE PEDIDOS")
print("------------------------------------------")

pedidos = obtener_informe_pedidos()

for pedido in pedidos:

    print(
        f"Cliente: {pedido['cliente']} | "
        f"Producto: {pedido['producto']} | "
        f"Cantidad: {pedido['cantidad']} | "
        f"Valor: Q{pedido['valor']}"
    )


# ==========================================================
# RESUMEN
# ==========================================================

print()
print("4. RESUMEN GENERAL")
print("------------------------------------------")

print(f"Cantidad de productos: {contar_productos()}")
print(f"Cantidad de clientes: {contar_clientes()}")
print(f"Cantidad de pedidos: {contar_pedidos()}")
print(f"Total de ventas: Q{calcular_total_ventas()}")


print()
print("==========================================")
print("PRUEBA DE INFORMES TERMINADA")
print("==========================================")