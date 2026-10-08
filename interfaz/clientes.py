"""
Interfaz gráfica para administrar clientes.
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

from funciones.clientes import (
    agregar_cliente,
    listar_clientes,
    buscar_cliente,
    editar_cliente,
    eliminar_cliente
)


class VentanaClientes(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Administración de Clientes"
        )

        self.setGeometry(
            200,
            100,
            900,
            600
        )

        self.crear_interfaz()

        self.cargar_clientes()


    # ======================================================
    # CREAR INTERFAZ
    # ======================================================

    def crear_interfaz(self):

        titulo = QLabel(
            "ADMINISTRACIÓN DE CLIENTES"
        )

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

        etiqueta_nombre = QLabel(
            "Nombre:"
        )

        etiqueta_nit = QLabel(
            "NIT:"
        )

        etiqueta_direccion = QLabel(
            "Dirección:"
        )


        self.campo_nombre = QLineEdit()

        self.campo_nit = QLineEdit()

        self.campo_direccion = QLineEdit()


        self.campo_nombre.setPlaceholderText(
            "Ingrese el nombre del cliente"
        )

        self.campo_nit.setPlaceholderText(
            "Ingrese el NIT"
        )

        self.campo_direccion.setPlaceholderText(
            "Ingrese la dirección"
        )


        # ==================================================
        # BOTONES
        # ==================================================

        boton_agregar = QPushButton(
            "Agregar"
        )

        boton_buscar = QPushButton(
            "Buscar"
        )

        boton_editar = QPushButton(
            "Editar"
        )

        boton_eliminar = QPushButton(
            "Eliminar"
        )

        boton_limpiar = QPushButton(
            "Limpiar"
        )

        boton_cerrar = QPushButton(
            "Cerrar"
        )


        # ==================================================
        # CONEXIONES
        # ==================================================

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

        self.tabla.setColumnCount(
            3
        )

        self.tabla.setHorizontalHeaderLabels([
            "Nombre",
            "NIT",
            "Dirección"
        ])

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabla.cellClicked.connect(
            self.seleccionar_cliente
        )


        # ==================================================
        # FILAS DE CAMPOS
        # ==================================================

        fila_nombre = QHBoxLayout()

        fila_nombre.addWidget(
            etiqueta_nombre
        )

        fila_nombre.addWidget(
            self.campo_nombre
        )


        fila_nit = QHBoxLayout()

        fila_nit.addWidget(
            etiqueta_nit
        )

        fila_nit.addWidget(
            self.campo_nit
        )


        fila_direccion = QHBoxLayout()

        fila_direccion.addWidget(
            etiqueta_direccion
        )

        fila_direccion.addWidget(
            self.campo_direccion
        )


        # ==================================================
        # FILA DE BOTONES
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
            fila_nit
        )

        layout.addLayout(
            fila_direccion
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
    # CARGAR CLIENTES
    # ======================================================

    def cargar_clientes(self):

        clientes = listar_clientes()

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


    # ======================================================
    # AGREGAR CLIENTE
    # ======================================================

    def agregar(self):

        nombre = self.campo_nombre.text().strip()

        nit = self.campo_nit.text().strip()

        direccion = self.campo_direccion.text().strip()


        if not nombre or not nit or not direccion:

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return


        if buscar_cliente(nombre):

            QMessageBox.warning(
                self,
                "Cliente existente",
                "Ya existe un cliente con ese nombre."
            )

            return


        agregar_cliente(
            nombre,
            nit,
            direccion
        )


        QMessageBox.information(
            self,
            "Cliente agregado",
            "El cliente se agregó correctamente."
        )


        self.limpiar()

        self.cargar_clientes()


    # ======================================================
    # BUSCAR CLIENTE
    # ======================================================

    def buscar(self):

        nombre = self.campo_nombre.text().strip()


        if not nombre:

            QMessageBox.warning(
                self,
                "Buscar cliente",
                "Ingrese el nombre del cliente."
            )

            return


        cliente = buscar_cliente(
            nombre
        )


        if cliente:

            self.campo_nombre.setText(
                str(cliente["nombre"])
            )

            self.campo_nit.setText(
                str(cliente["nit"])
            )

            self.campo_direccion.setText(
                str(cliente["direccion"])
            )


            QMessageBox.information(
                self,
                "Cliente encontrado",
                "Cliente encontrado correctamente."
            )

        else:

            QMessageBox.warning(
                self,
                "Cliente no encontrado",
                "No existe un cliente con ese nombre."
            )


    # ======================================================
    # EDITAR CLIENTE
    # ======================================================

    def editar(self):

        nombre_actual = self.campo_nombre.text().strip()

        nuevo_nombre = self.campo_nombre.text().strip()

        nuevo_nit = self.campo_nit.text().strip()

        nueva_direccion = self.campo_direccion.text().strip()


        if (
            not nombre_actual
            or not nuevo_nit
            or not nueva_direccion
        ):

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Complete los datos del cliente."
            )

            return


        resultado = editar_cliente(
            nombre_actual,
            nuevo_nombre,
            nuevo_nit,
            nueva_direccion
        )


        if resultado:

            QMessageBox.information(
                self,
                "Cliente editado",
                "Cliente editado correctamente."
            )

            self.limpiar()

            self.cargar_clientes()

        else:

            QMessageBox.warning(
                self,
                "Cliente no encontrado",
                "No se encontró el cliente."
            )


    # ======================================================
    # ELIMINAR CLIENTE
    # ======================================================

    def eliminar(self):

        nombre = self.campo_nombre.text().strip()


        if not nombre:

            QMessageBox.warning(
                self,
                "Eliminar cliente",
                "Ingrese el nombre del cliente."
            )

            return


        cliente = buscar_cliente(
            nombre
        )


        if not cliente:

            QMessageBox.warning(
                self,
                "Cliente no encontrado",
                "No existe un cliente con ese nombre."
            )

            return


        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de eliminar el cliente '{nombre}'?",
            QMessageBox.Yes | QMessageBox.No
        )


        if confirmacion == QMessageBox.Yes:

            resultado = eliminar_cliente(
                nombre
            )


            if resultado:

                QMessageBox.information(
                    self,
                    "Cliente eliminado",
                    "Cliente eliminado correctamente."
                )

                self.limpiar()

                self.cargar_clientes()


    # ======================================================
    # SELECCIONAR CLIENTE
    # ======================================================

    def seleccionar_cliente(
        self,
        fila,
        columna
    ):

        nombre = self.tabla.item(
            fila,
            0
        ).text()

        nit = self.tabla.item(
            fila,
            1
        ).text()

        direccion = self.tabla.item(
            fila,
            2
        ).text()


        self.campo_nombre.setText(
            nombre
        )

        self.campo_nit.setText(
            nit
        )

        self.campo_direccion.setText(
            direccion
        )


    # ======================================================
    # LIMPIAR
    # ======================================================

    def limpiar(self):

        self.campo_nombre.clear()

        self.campo_nit.clear()

        self.campo_direccion.clear()

        self.campo_nombre.setFocus()