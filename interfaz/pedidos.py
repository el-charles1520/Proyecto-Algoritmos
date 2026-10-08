"""
Interfaz gráfica para administrar pedidos.
"""

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QHeaderView
)

from funciones.pedidos import (
    agregar_pedido,
    listar_pedidos,
    buscar_pedidos_cliente,
    eliminar_pedido
)


class VentanaPedidos(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Administración de Pedidos"
        )

        self.setGeometry(
            200,
            100,
            950,
            600
        )

        self.crear_interfaz()

        self.cargar_pedidos()


    def crear_interfaz(self):

        titulo = QLabel(
            "ADMINISTRACIÓN DE PEDIDOS"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        etiqueta_cliente = QLabel("Cliente:")
        etiqueta_producto = QLabel("Producto:")
        etiqueta_cantidad = QLabel("Cantidad:")

        self.campo_cliente = QLineEdit()
        self.campo_producto = QLineEdit()
        self.campo_cantidad = QLineEdit()

        self.campo_cliente.setPlaceholderText(
            "Ingrese el nombre del cliente"
        )

        self.campo_producto.setPlaceholderText(
            "Ingrese el nombre del producto"
        )

        self.campo_cantidad.setPlaceholderText(
            "Ingrese la cantidad"
        )

        boton_agregar = QPushButton("Agregar")
        boton_buscar = QPushButton("Buscar")
        boton_eliminar = QPushButton("Eliminar")
        boton_limpiar = QPushButton("Limpiar")
        boton_cerrar = QPushButton("Cerrar")

        boton_agregar.clicked.connect(
            self.agregar
        )

        boton_buscar.clicked.connect(
            self.buscar
        )

        boton_eliminar.clicked.connect(
            self.eliminar
        )

        boton_limpiar.clicked.connect(
            self.limpiar
        )

        boton_cerrar.clicked.connect(
            self.close
        )

        self.tabla = QTableWidget()

        self.tabla.setColumnCount(4)

        self.tabla.setHorizontalHeaderLabels([
            "Cliente",
            "Producto",
            "Cantidad",
            "Valor"
        ])

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabla.cellClicked.connect(
            self.seleccionar_pedido
        )

        fila_cliente = QHBoxLayout()

        fila_cliente.addWidget(
            etiqueta_cliente
        )

        fila_cliente.addWidget(
            self.campo_cliente
        )


        fila_producto = QHBoxLayout()

        fila_producto.addWidget(
            etiqueta_producto
        )

        fila_producto.addWidget(
            self.campo_producto
        )


        fila_cantidad = QHBoxLayout()

        fila_cantidad.addWidget(
            etiqueta_cantidad
        )

        fila_cantidad.addWidget(
            self.campo_cantidad
        )


        fila_botones = QHBoxLayout()

        fila_botones.addWidget(
            boton_agregar
        )

        fila_botones.addWidget(
            boton_buscar
        )

        fila_botones.addWidget(
            boton_eliminar
        )

        fila_botones.addWidget(
            boton_limpiar
        )

        fila_botones.addWidget(
            boton_cerrar
        )


        layout = QVBoxLayout()

        layout.addWidget(
            titulo
        )

        layout.addLayout(
            fila_cliente
        )

        layout.addLayout(
            fila_producto
        )

        layout.addLayout(
            fila_cantidad
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


    def cargar_pedidos(self):

        pedidos = listar_pedidos()

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


    def agregar(self):

        cliente = self.campo_cliente.text().strip()
        producto = self.campo_producto.text().strip()
        cantidad = self.campo_cantidad.text().strip()

        if not cliente or not producto or not cantidad:

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return


        try:

            cantidad = int(cantidad)

        except ValueError:

            QMessageBox.warning(
                self,
                "Cantidad incorrecta",
                "La cantidad debe ser un número entero."
            )

            return


        if cantidad <= 0:

            QMessageBox.warning(
                self,
                "Cantidad incorrecta",
                "La cantidad debe ser mayor que cero."
            )

            return


        resultado = agregar_pedido(
            cliente,
            producto,
            cantidad
        )


        if resultado:

            QMessageBox.information(
                self,
                "Pedido agregado",
                "El pedido se agregó correctamente."
            )

            self.limpiar()

            self.cargar_pedidos()

        else:

            QMessageBox.warning(
                self,
                "Producto no encontrado",
                "El producto indicado no existe."
            )


    def buscar(self):

        cliente = self.campo_cliente.text().strip()

        if not cliente:

            QMessageBox.warning(
                self,
                "Buscar pedidos",
                "Ingrese el nombre del cliente."
            )

            return


        pedidos = buscar_pedidos_cliente(
            cliente
        )


        if pedidos:

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

        else:

            QMessageBox.warning(
                self,
                "Pedidos no encontrados",
                "No existen pedidos para ese cliente."
            )


    def eliminar(self):

        cliente = self.campo_cliente.text().strip()
        producto = self.campo_producto.text().strip()

        if not cliente or not producto:

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Ingrese el cliente y el producto."
            )

            return


        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el pedido de "
            f"'{cliente}' correspondiente a '{producto}'?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirmacion == QMessageBox.Yes:

            resultado = eliminar_pedido(
                cliente,
                producto
            )


            if resultado:

                QMessageBox.information(
                    self,
                    "Pedido eliminado",
                    "El pedido se eliminó correctamente."
                )

                self.limpiar()

                self.cargar_pedidos()

            else:

                QMessageBox.warning(
                    self,
                    "Pedido no encontrado",
                    "No se encontró el pedido."
                )


    def seleccionar_pedido(
        self,
        fila,
        columna
    ):

        cliente = self.tabla.item(
            fila,
            0
        ).text()

        producto = self.tabla.item(
            fila,
            1
        ).text()

        cantidad = self.tabla.item(
            fila,
            2
        ).text()

        self.campo_cliente.setText(
            cliente
        )

        self.campo_producto.setText(
            producto
        )

        self.campo_cantidad.setText(
            cantidad
        )


    def limpiar(self):

        self.campo_cliente.clear()

        self.campo_producto.clear()

        self.campo_cantidad.clear()

        self.campo_cliente.setFocus()