"""
Interfaz gráfica para administrar productos.
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

from funciones.productos import (
    agregar_producto,
    listar_productos,
    buscar_producto,
    editar_producto,
    eliminar_producto
)


class VentanaProductos(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Administración de Productos")
        self.setGeometry(200, 100, 900, 600)

        self.crear_interfaz()

        self.cargar_productos()


    def crear_interfaz(self):

        # ==================================================
        # TÍTULO
        # ==================================================

        titulo = QLabel("ADMINISTRACIÓN DE PRODUCTOS")

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
            }
        """)


        # ==================================================
        # CAMPOS
        # ==================================================

        etiqueta_nombre = QLabel("Nombre:")
        etiqueta_precio = QLabel("Precio:")
        etiqueta_existencia = QLabel("Existencia:")

        self.campo_nombre = QLineEdit()
        self.campo_precio = QLineEdit()
        self.campo_existencia = QLineEdit()

        self.campo_nombre.setPlaceholderText(
            "Ingrese el nombre del producto"
        )

        self.campo_precio.setPlaceholderText(
            "Ingrese el precio"
        )

        self.campo_existencia.setPlaceholderText(
            "Ingrese la existencia"
        )


        # ==================================================
        # BOTONES
        # ==================================================

        boton_agregar = QPushButton("Agregar")

        boton_buscar = QPushButton("Buscar")

        boton_editar = QPushButton("Editar")

        boton_eliminar = QPushButton("Eliminar")

        boton_limpiar = QPushButton("Limpiar")

        boton_cerrar = QPushButton("Cerrar")


        # Conectar botones

        boton_agregar.clicked.connect(
            self.agregar
        )

        boton_buscar.clicked.connect(
            self.buscar
        )

        boton_editar.clicked.connect(
            self.editar
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


        # ==================================================
        # TABLA
        # ==================================================

        self.tabla = QTableWidget()

        self.tabla.setColumnCount(3)

        self.tabla.setHorizontalHeaderLabels([
            "Nombre",
            "Precio",
            "Existencia"
        ])

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabla.cellClicked.connect(
            self.seleccionar_producto
        )


        # ==================================================
        # DISEÑO DE CAMPOS
        # ==================================================

        fila_nombre = QHBoxLayout()

        fila_nombre.addWidget(
            etiqueta_nombre
        )

        fila_nombre.addWidget(
            self.campo_nombre
        )


        fila_precio = QHBoxLayout()

        fila_precio.addWidget(
            etiqueta_precio
        )

        fila_precio.addWidget(
            self.campo_precio
        )


        fila_existencia = QHBoxLayout()

        fila_existencia.addWidget(
            etiqueta_existencia
        )

        fila_existencia.addWidget(
            self.campo_existencia
        )


        # ==================================================
        # DISEÑO DE BOTONES
        # ==================================================

        fila_botones = QHBoxLayout()

        fila_botones.addWidget(
            boton_agregar
        )

        fila_botones.addWidget(
            boton_buscar
        )

        fila_botones.addWidget(
            boton_editar
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


        # ==================================================
        # DISEÑO PRINCIPAL
        # ==================================================

        layout = QVBoxLayout()

        layout.addWidget(
            titulo
        )

        layout.addLayout(
            fila_nombre
        )

        layout.addLayout(
            fila_precio
        )

        layout.addLayout(
            fila_existencia
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


    # ======================================================
    # CARGAR PRODUCTOS
    # ======================================================

    def cargar_productos(self):

        productos = listar_productos()

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


    # ======================================================
    # AGREGAR
    # ======================================================

    def agregar(self):

        nombre = self.campo_nombre.text().strip()
        precio = self.campo_precio.text().strip()
        existencia = self.campo_existencia.text().strip()


        if not nombre or not precio or not existencia:

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return


        try:

            precio = float(precio)
            existencia = int(existencia)

        except ValueError:

            QMessageBox.warning(
                self,
                "Datos incorrectos",
                "El precio debe ser numérico y la existencia debe ser un número entero."
            )

            return


        if precio < 0 or existencia < 0:

            QMessageBox.warning(
                self,
                "Datos incorrectos",
                "El precio y la existencia no pueden ser negativos."
            )

            return


        if buscar_producto(nombre):

            QMessageBox.warning(
                self,
                "Producto existente",
                "Ya existe un producto con ese nombre."
            )

            return


        agregar_producto(
            nombre,
            precio,
            existencia
        )


        QMessageBox.information(
            self,
            "Producto agregado",
            "El producto se agregó correctamente."
        )


        self.limpiar()

        self.cargar_productos()


    # ======================================================
    # BUSCAR
    # ======================================================

    def buscar(self):

        nombre = self.campo_nombre.text().strip()


        if not nombre:

            QMessageBox.warning(
                self,
                "Buscar producto",
                "Ingrese el nombre del producto."
            )

            return


        producto = buscar_producto(
            nombre
        )


        if producto:

            self.campo_nombre.setText(
                str(producto["nombre"])
            )

            self.campo_precio.setText(
                str(producto["precio"])
            )

            self.campo_existencia.setText(
                str(producto["existencia"])
            )


            QMessageBox.information(
                self,
                "Producto encontrado",
                "Producto encontrado correctamente."
            )

        else:

            QMessageBox.warning(
                self,
                "Producto no encontrado",
                "No existe un producto con ese nombre."
            )


    # ======================================================
    # EDITAR
    # ======================================================

    def editar(self):

        nombre_actual = self.campo_nombre.text().strip()
        nuevo_nombre = self.campo_nombre.text().strip()
        nuevo_precio = self.campo_precio.text().strip()
        nueva_existencia = self.campo_existencia.text().strip()


        if not nombre_actual or not nuevo_precio or not nueva_existencia:

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Complete los datos del producto."
            )

            return


        try:

            nuevo_precio = float(nuevo_precio)
            nueva_existencia = int(nueva_existencia)

        except ValueError:

            QMessageBox.warning(
                self,
                "Datos incorrectos",
                "El precio debe ser numérico y la existencia debe ser un número entero."
            )

            return


        resultado = editar_producto(
            nombre_actual,
            nuevo_nombre,
            nuevo_precio,
            nueva_existencia
        )


        if resultado:

            QMessageBox.information(
                self,
                "Producto editado",
                "Producto editado correctamente."
            )

            self.limpiar()

            self.cargar_productos()

        else:

            QMessageBox.warning(
                self,
                "Producto no encontrado",
                "No se encontró el producto."
            )


    # ======================================================
    # ELIMINAR
    # ======================================================

    def eliminar(self):

        nombre = self.campo_nombre.text().strip()


        if not nombre:

            QMessageBox.warning(
                self,
                "Eliminar producto",
                "Ingrese el nombre del producto."
            )

            return


        producto = buscar_producto(
            nombre
        )


        if not producto:

            QMessageBox.warning(
                self,
                "Producto no encontrado",
                "No existe un producto con ese nombre."
            )

            return


        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el producto '{nombre}'?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirmacion == QMessageBox.Yes:

            resultado = eliminar_producto(
                nombre
            )


            if resultado:

                QMessageBox.information(
                    self,
                    "Producto eliminado",
                    "Producto eliminado correctamente."
                )

                self.limpiar()

                self.cargar_productos()


    # ======================================================
    # SELECCIONAR PRODUCTO DE LA TABLA
    # ======================================================

    def seleccionar_producto(
        self,
        fila,
        columna
    ):

        nombre = self.tabla.item(
            fila,
            0
        ).text()

        precio = self.tabla.item(
            fila,
            1
        ).text()

        existencia = self.tabla.item(
            fila,
            2
        ).text()


        self.campo_nombre.setText(
            nombre
        )

        self.campo_precio.setText(
            precio
        )

        self.campo_existencia.setText(
            existencia
        )


    # ======================================================
    # LIMPIAR
    # ======================================================

    def limpiar(self):

        self.campo_nombre.clear()

        self.campo_precio.clear()

        self.campo_existencia.clear()

        self.campo_nombre.setFocus()