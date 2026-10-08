"""
Pruebas de los módulos de productos, clientes y pedidos.
"""

import sys
from pathlib import Path

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CARPETA_PROYECTO))


from funciones.productos import (
    agregar_producto,
    listar_productos,
    buscar_producto,
    editar_producto,
    eliminar_producto
)

from funciones.clientes import (
    agregar_cliente,
    listar_clientes,
    buscar_cliente,
    editar_cliente,
    eliminar_cliente
)

from funciones.pedidos import (
    agregar_pedido,
    listar_pedidos,
    buscar_pedidos_cliente,
    eliminar_pedido
)


# ==========================================================
# PRUEBA DE PRODUCTOS
# ==========================================================

def probar_productos():

    print()
    print("==========================================")
    print("PRUEBA DEL MÓDULO DE PRODUCTOS")
    print("==========================================")

    # ------------------------------------------------------
    # 1. Agregar producto
    # ------------------------------------------------------

    print()
    print("1. Agregando producto...")

    agregar_producto(
        "Audífonos",
        250,
        10
    )

    print("Producto agregado correctamente.")

    # ------------------------------------------------------
    # 2. Buscar producto
    # ------------------------------------------------------

    print()
    print("2. Buscando producto...")

    producto = buscar_producto(
        "Audífonos"
    )

    if producto:
        print("Producto encontrado correctamente.")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: Q{producto['precio']}")
        print(f"Existencia: {producto['existencia']}")
    else:
        print("Producto no encontrado.")

    # ------------------------------------------------------
    # 3. Editar producto
    # ------------------------------------------------------

    print()
    print("3. Editando producto...")

    resultado = editar_producto(
        "Audífonos",
        "Audífonos Bluetooth",
        300,
        15
    )

    if resultado:
        print("Producto editado correctamente.")
    else:
        print("No se encontró el producto.")

    # ------------------------------------------------------
    # 4. Verificar producto editado
    # ------------------------------------------------------

    print()
    print("4. Verificando producto editado...")

    producto = buscar_producto(
        "Audífonos Bluetooth"
    )

    if producto:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: Q{producto['precio']}")
        print(f"Existencia: {producto['existencia']}")
    else:
        print("Producto editado no encontrado.")

    # ------------------------------------------------------
    # 5. Eliminar producto
    # ------------------------------------------------------

    print()
    print("5. Eliminando producto...")

    resultado = eliminar_producto(
        "Audífonos Bluetooth"
    )

    if resultado:
        print("Producto eliminado correctamente.")
    else:
        print("No se encontró el producto.")

    # ------------------------------------------------------
    # 6. Mostrar productos actuales
    # ------------------------------------------------------

    print()
    print("6. Productos actuales:")

    productos = listar_productos()

    for producto in productos:
        print(
            f"{producto['nombre']} | "
            f"Q{producto['precio']} | "
            f"{producto['existencia']}"
        )

    print()
    print("==========================================")
    print("PRUEBA DE PRODUCTOS TERMINADA")
    print("==========================================")


# ==========================================================
# PRUEBA DE CLIENTES
# ==========================================================

def probar_clientes():

    print()
    print("==========================================")
    print("PRUEBA DEL MÓDULO DE CLIENTES")
    print("==========================================")

    # ------------------------------------------------------
    # 1. Agregar cliente
    # ------------------------------------------------------

    print()
    print("1. Agregando cliente...")

    agregar_cliente(
        "Carlos Pérez",
        "555555-5",
        "Jalapa"
    )

    print("Cliente agregado correctamente.")

    # ------------------------------------------------------
    # 2. Mostrar clientes
    # ------------------------------------------------------

    print()
    print("2. Lista de clientes:")

    clientes = listar_clientes()

    for cliente in clientes:
        print(
            f"Nombre: {cliente['nombre']} | "
            f"NIT: {cliente['nit']} | "
            f"Dirección: {cliente['direccion']}"
        )

    # ------------------------------------------------------
    # 3. Buscar cliente
    # ------------------------------------------------------

    print()
    print("3. Buscando cliente...")

    cliente = buscar_cliente(
        "Carlos Pérez"
    )

    if cliente:
        print("Cliente encontrado.")
        print(f"Nombre: {cliente['nombre']}")
        print(f"NIT: {cliente['nit']}")
        print(f"Dirección: {cliente['direccion']}")
    else:
        print("Cliente no encontrado.")

    # ------------------------------------------------------
    # 4. Editar cliente
    # ------------------------------------------------------

    print()
    print("4. Editando cliente...")

    resultado = editar_cliente(
        "Carlos Pérez",
        "Carlos Pérez Santiago",
        "666666-6",
        "Guatemala"
    )

    if resultado:
        print("Cliente editado correctamente.")
    else:
        print("No se encontró el cliente.")

    # ------------------------------------------------------
    # 5. Verificar cliente editado
    # ------------------------------------------------------

    print()
    print("5. Verificando cliente editado...")

    cliente = buscar_cliente(
        "Carlos Pérez Santiago"
    )

    if cliente:
        print(f"Nombre: {cliente['nombre']}")
        print(f"NIT: {cliente['nit']}")
        print(f"Dirección: {cliente['direccion']}")
    else:
        print("Cliente editado no encontrado.")

    # ------------------------------------------------------
    # 6. Eliminar cliente
    # ------------------------------------------------------

    print()
    print("6. Eliminando cliente...")

    resultado = eliminar_cliente(
        "Carlos Pérez Santiago"
    )

    if resultado:
        print("Cliente eliminado correctamente.")
    else:
        print("No se encontró el cliente.")

    # ------------------------------------------------------
    # 7. Mostrar lista final
    # ------------------------------------------------------

    print()
    print("7. Lista final de clientes:")

    clientes = listar_clientes()

    for cliente in clientes:
        print(
            f"Nombre: {cliente['nombre']} | "
            f"NIT: {cliente['nit']} | "
            f"Dirección: {cliente['direccion']}"
        )

    print()
    print("==========================================")
    print("PRUEBA DE CLIENTES TERMINADA")
    print("==========================================")


# ==========================================================
# PRUEBA DE PEDIDOS
# ==========================================================

def probar_pedidos():

    print()
    print("==========================================")
    print("PRUEBA DEL MÓDULO DE PEDIDOS")
    print("==========================================")

    # ------------------------------------------------------
    # 1. Agregar pedido de prueba
    # ------------------------------------------------------

    print()
    print("1. Agregando pedido de prueba...")

    resultado = agregar_pedido(
        "Juan Pérez",
        "Mouse",
        3
    )

    if resultado:
        print("Pedido agregado correctamente.")
    else:
        print("No se pudo agregar el pedido.")

    # ------------------------------------------------------
    # 2. Mostrar pedidos
    # ------------------------------------------------------

    print()
    print("2. Lista de pedidos:")

    pedidos = listar_pedidos()

    for pedido in pedidos:
        print(
            f"Cliente: {pedido['cliente']} | "
            f"Producto: {pedido['producto']} | "
            f"Cantidad: {pedido['cantidad']} | "
            f"Valor: Q{pedido['valor']}"
        )

    # ------------------------------------------------------
    # 3. Buscar pedidos por cliente
    # ------------------------------------------------------

    print()
    print("3. Buscando pedidos de Juan Pérez...")

    pedidos_cliente = buscar_pedidos_cliente(
        "Juan Pérez"
    )

    if pedidos_cliente:

        for pedido in pedidos_cliente:
            print(
                f"Producto: {pedido['producto']} | "
                f"Cantidad: {pedido['cantidad']} | "
                f"Valor: Q{pedido['valor']}"
            )

    else:
        print("El cliente no tiene pedidos.")

    # ------------------------------------------------------
    # 4. Eliminar SOLO el pedido de prueba
    # ------------------------------------------------------

    print()
    print("4. Eliminando pedido de prueba...")

    resultado = eliminar_pedido(
        "Juan Pérez",
        "Mouse"
    )

    if resultado:
        print("Pedido de prueba eliminado correctamente.")
    else:
        print("No se encontró el pedido de prueba.")

    # ------------------------------------------------------
    # 5. Mostrar pedidos finales
    # ------------------------------------------------------

    print()
    print("5. Lista final de pedidos:")

    pedidos = listar_pedidos()

    for pedido in pedidos:
        print(
            f"Cliente: {pedido['cliente']} | "
            f"Producto: {pedido['producto']} | "
            f"Cantidad: {pedido['cantidad']} | "
            f"Valor: Q{pedido['valor']}"
        )

    print()
    print("==========================================")
    print("PRUEBA DE PEDIDOS TERMINADA")
    print("==========================================")


# ==========================================================
# EJECUCIÓN GENERAL
# ==========================================================

if __name__ == "__main__":

    probar_productos()

    probar_clientes()

    probar_pedidos()

    print()
    print("==========================================")
    print("TODAS LAS PRUEBAS TERMINARON")
    print("==========================================")