"""
Menú principal del sistema.
"""

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from interfaz.productos import VentanaProductos
from interfaz.clientes import VentanaClientes
from interfaz.pedidos import VentanaPedidos
from interfaz.informes import VentanaInformes
from interfaz.cotizacion import VentanaCotizacion

from funciones.respaldo import crear_respaldo


class VentanaPrincipal(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Sistema de Gestión"
        )

        self.setGeometry(
            300,
            100,
            500,
            600
        )

        self.ventana_productos = None
        self.ventana_clientes = None
        self.ventana_pedidos = None
        self.ventana_informes = None
        self.ventana_cotizacion = None

        self.crear_interfaz()


    def crear_interfaz(self):

        titulo = QLabel(
            "SISTEMA DE GESTIÓN"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 26px;
                font-weight: bold;
                padding: 20px;
            }
        """)


        boton_productos = QPushButton(
            "PRODUCTOS"
        )

        boton_clientes = QPushButton(
            "CLIENTES"
        )

        boton_pedidos = QPushButton(
            "PEDIDOS"
        )

        boton_informes = QPushButton(
            "INFORMES"
        )

        boton_cotizacion = QPushButton(
            "COTIZACIÓN"
        )

        boton_respaldo = QPushButton(
            "RESPALDO"
        )

        boton_salir = QPushButton(
            "SALIR"
        )


        boton_productos.clicked.connect(
            self.abrir_productos
        )

        boton_clientes.clicked.connect(
            self.abrir_clientes
        )

        boton_pedidos.clicked.connect(
            self.abrir_pedidos
        )

        boton_informes.clicked.connect(
            self.abrir_informes
        )

        boton_cotizacion.clicked.connect(
            self.abrir_cotizacion
        )

        boton_respaldo.clicked.connect(
            self.crear_respaldo
        )

        boton_salir.clicked.connect(
            self.close
        )


        layout = QVBoxLayout()

        layout.addWidget(
            titulo
        )

        layout.addSpacing(
            20
        )

        layout.addWidget(
            boton_productos
        )

        layout.addWidget(
            boton_clientes
        )

        layout.addWidget(
            boton_pedidos
        )

        layout.addWidget(
            boton_informes
        )

        layout.addWidget(
            boton_cotizacion
        )

        layout.addWidget(
            boton_respaldo
        )

        layout.addSpacing(
            20
        )

        layout.addWidget(
            boton_salir
        )

        self.setLayout(
            layout
        )


    def abrir_productos(self):

        self.ventana_productos = VentanaProductos()

        self.ventana_productos.show()


    def abrir_clientes(self):

        self.ventana_clientes = VentanaClientes()

        self.ventana_clientes.show()


    def abrir_pedidos(self):

        self.ventana_pedidos = VentanaPedidos()

        self.ventana_pedidos.show()


    def abrir_informes(self):

        self.ventana_informes = VentanaInformes()

        self.ventana_informes.show()


    def abrir_cotizacion(self):

        self.ventana_cotizacion = VentanaCotizacion()

        self.ventana_cotizacion.show()


    def crear_respaldo(self):

        try:

            ruta = crear_respaldo()

            if ruta is not None:

                QMessageBox.information(
                    self,
                    "Respaldo creado",
                    "La copia de seguridad se creó correctamente.\n\n"
                    f"Archivo:\n{ruta}"
                )

            else:

                QMessageBox.warning(
                    self,
                    "Error",
                    "No se encontró el archivo Inventario.xlsx."
                )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Error",
                "No fue posible crear el respaldo.\n\n"
                f"Error: {error}"
            )

