"""
Interfaz gráfica para consultar informes.
"""

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QHeaderView
)

from funciones.informes import (
    obtener_informe_productos,
    obtener_informe_clientes,
    obtener_informe_pedidos,
    calcular_total_ventas,
    contar_productos,
    contar_clientes,
    contar_pedidos
)


class VentanaInformes(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Informes del Sistema"
        )

        self.setGeometry(
            150,
            100,
            1000,
            650
        )

        self.crear_interfaz()

        self.mostrar_productos()


    def crear_interfaz(self):

        titulo = QLabel(
            "INFORMES DEL SISTEMA"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 26px;
                font-weight: bold;
                padding: 15px;
            }
        """)


        self.label_resumen = QLabel()

        self.label_resumen.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 10px;
            }
        """)


        boton_productos = QPushButton(
            "Productos"
        )

        boton_clientes = QPushButton(
            "Clientes"
        )

        boton_pedidos = QPushButton(
            "Pedidos"
        )

        boton_resumen = QPushButton(
            "Resumen"
        )

        boton_cerrar = QPushButton(
            "Cerrar"
        )


        boton_productos.clicked.connect(
            self.mostrar_productos
        )

        boton_clientes.clicked.connect(
            self.mostrar_clientes
        )

        boton_pedidos.clicked.connect(
            self.mostrar_pedidos
        )

        boton_resumen.clicked.connect(
            self.mostrar_resumen
        )

        boton_cerrar.clicked.connect(
            self.close
        )


        fila_botones = QHBoxLayout()

        fila_botones.addWidget(
            boton_productos
        )

        fila_botones.addWidget(
            boton_clientes
        )

        fila_botones.addWidget(
            boton_pedidos
        )

        fila_botones.addWidget(
            boton_resumen
        )

        fila_botones.addWidget(
            boton_cerrar
        )


        self.tabla = QTableWidget()

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )


        layout = QVBoxLayout()

        layout.addWidget(
            titulo
        )

        layout.addWidget(
            self.label_resumen
        )

        layout.addLayout(
            fila_botones
        )

        layout.addWidget(
            self.tabla
        )


        self.setLayout(
            layout
        )


    def mostrar_productos(self):

        productos = obtener_informe_productos()

        self.tabla.clear()

        self.tabla.setColumnCount(3)

        self.tabla.setHorizontalHeaderLabels([
            "Nombre",
            "Precio",
            "Existencia"
        ])

        self.tabla.setRowCount(
            len(productos)
        )


        for fila, producto in enumerate(productos):

            self.tabla.setItem(
                fila,
                0,
                QTableWidgetItem(
                    str(producto["nombre"])
                )
            )

            self.tabla.setItem(
                fila,
                1,
                QTableWidgetItem(
                    str(producto["precio"])
                )
            )

            self.tabla.setItem(
                fila,
                2,
                QTableWidgetItem(
                    str(producto["existencia"])
                )
            )


        self.label_resumen.setText(
            f"Total de productos registrados: "
            f"{contar_productos()}"
        )


    def mostrar_clientes(self):

        clientes = obtener_informe_clientes()

        self.tabla.clear()

        self.tabla.setColumnCount(3)

        self.tabla.setHorizontalHeaderLabels([
            "Nombre",
            "NIT",
            "Dirección"
        ])

        self.tabla.setRowCount(
            len(clientes)
        )


        for fila, cliente in enumerate(clientes):

            self.tabla.setItem(
                fila,
                0,
                QTableWidgetItem(
                    str(cliente["nombre"])
                )
            )

            self.tabla.setItem(
                fila,
                1,
                QTableWidgetItem(
                    str(cliente["nit"])
                )
            )

            self.tabla.setItem(
                fila,
                2,
                QTableWidgetItem(
                    str(cliente["direccion"])
                )
            )


        self.label_resumen.setText(
            f"Total de clientes registrados: "
            f"{contar_clientes()}"
        )


    def mostrar_pedidos(self):

        pedidos = obtener_informe_pedidos()

        self.tabla.clear()

        self.tabla.setColumnCount(4)

        self.tabla.setHorizontalHeaderLabels([
            "Cliente",
            "Producto",
            "Cantidad",
            "Valor"
        ])

        self.tabla.setRowCount(
            len(pedidos)
        )


        for fila, pedido in enumerate(pedidos):

            self.tabla.setItem(
                fila,
                0,
                QTableWidgetItem(
                    str(pedido["cliente"])
                )
            )

            self.tabla.setItem(
                fila,
                1,
                QTableWidgetItem(
                    str(pedido["producto"])
                )
            )

            self.tabla.setItem(
                fila,
                2,
                QTableWidgetItem(
                    str(pedido["cantidad"])
                )
            )

            self.tabla.setItem(
                fila,
                3,
                QTableWidgetItem(
                    str(pedido["valor"])
                )
            )


        self.label_resumen.setText(
            f"Total de pedidos registrados: "
            f"{contar_pedidos()}"
        )


    def mostrar_resumen(self):

        self.tabla.clear()

        self.tabla.setColumnCount(2)

        self.tabla.setHorizontalHeaderLabels([
            "Indicador",
            "Valor"
        ])

        self.tabla.setRowCount(4)


        self.tabla.setItem(
            0,
            0,
            QTableWidgetItem(
                "Productos registrados"
            )
        )

        self.tabla.setItem(
            0,
            1,
            QTableWidgetItem(
                str(contar_productos())
            )
        )


        self.tabla.setItem(
            1,
            0,
            QTableWidgetItem(
                "Clientes registrados"
            )
        )

        self.tabla.setItem(
            1,
            1,
            QTableWidgetItem(
                str(contar_clientes())
            )
        )


        self.tabla.setItem(
            2,
            0,
            QTableWidgetItem(
                "Pedidos registrados"
            )
        )

        self.tabla.setItem(
            2,
            1,
            QTableWidgetItem(
                str(contar_pedidos())
            )
        )


        self.tabla.setItem(
            3,
            0,
            QTableWidgetItem(
                "Total de ventas"
            )
        )

        self.tabla.setItem(
            3,
            1,
            QTableWidgetItem(
                f"Q{calcular_total_ventas():.2f}"
            )
        )


        self.label_resumen.setText(
            "RESUMEN GENERAL DEL SISTEMA"
        )