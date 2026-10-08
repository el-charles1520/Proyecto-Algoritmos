"""
Interfaz gráfica para generar y enviar cotizaciones.
"""

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from funciones.cotizacion import generar_cotizacion
from funciones.correo import enviar_correo


class VentanaCotizacion(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Generar Cotización"
        )

        self.setGeometry(
            250,
            100,
            700,
            680
        )

        self.crear_interfaz()


    def crear_interfaz(self):

        titulo = QLabel(
            "GENERAR COTIZACIÓN"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 26px;
                font-weight: bold;
                padding: 15px;
            }
        """)


        etiqueta_cliente = QLabel(
            "Cliente:"
        )

        etiqueta_correo = QLabel(
            "Correo:"
        )

        etiqueta_nit = QLabel(
            "NIT:"
        )

        etiqueta_direccion = QLabel(
            "Dirección:"
        )

        etiqueta_producto = QLabel(
            "Producto:"
        )

        etiqueta_cantidad = QLabel(
            "Cantidad:"
        )

        etiqueta_precio = QLabel(
            "Precio:"
        )


        self.campo_cliente = QLineEdit()

        self.campo_correo = QLineEdit()

        self.campo_nit = QLineEdit()

        self.campo_direccion = QLineEdit()

        self.campo_producto = QLineEdit()

        self.campo_cantidad = QLineEdit()

        self.campo_precio = QLineEdit()


        self.campo_cliente.setPlaceholderText(
            "Ingrese el nombre del cliente"
        )

        self.campo_correo.setPlaceholderText(
            "Ingrese el correo electrónico"
        )

        self.campo_nit.setPlaceholderText(
            "Ingrese el NIT"
        )

        self.campo_direccion.setPlaceholderText(
            "Ingrese la dirección"
        )

        self.campo_producto.setPlaceholderText(
            "Ingrese el producto"
        )

        self.campo_cantidad.setPlaceholderText(
            "Ingrese la cantidad"
        )

        self.campo_precio.setPlaceholderText(
            "Ingrese el precio"
        )


        boton_generar = QPushButton(
            "GENERAR COTIZACIÓN"
        )

        boton_enviar = QPushButton(
            "ENVIAR COTIZACIÓN"
        )

        boton_limpiar = QPushButton(
            "LIMPIAR"
        )

        boton_cerrar = QPushButton(
            "CERRAR"
        )


        boton_generar.clicked.connect(
            self.generar
        )

        boton_enviar.clicked.connect(
            self.enviar_cotizacion
        )

        boton_limpiar.clicked.connect(
            self.limpiar
        )

        boton_cerrar.clicked.connect(
            self.close
        )


        fila_cliente = QHBoxLayout()

        fila_cliente.addWidget(
            etiqueta_cliente
        )

        fila_cliente.addWidget(
            self.campo_cliente
        )


        fila_correo = QHBoxLayout()

        fila_correo.addWidget(
            etiqueta_correo
        )

        fila_correo.addWidget(
            self.campo_correo
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


        fila_precio = QHBoxLayout()

        fila_precio.addWidget(
            etiqueta_precio
        )

        fila_precio.addWidget(
            self.campo_precio
        )


        fila_botones = QHBoxLayout()

        fila_botones.addWidget(
            boton_generar
        )

        fila_botones.addWidget(
            boton_enviar
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
            fila_correo
        )

        layout.addLayout(
            fila_nit
        )

        layout.addLayout(
            fila_direccion
        )

        layout.addLayout(
            fila_producto
        )

        layout.addLayout(
            fila_cantidad
        )

        layout.addLayout(
            fila_precio
        )

        layout.addSpacing(
            20
        )

        layout.addLayout(
            fila_botones
        )


        self.setLayout(
            layout
        )


    def obtener_datos(self):

        cliente = (
            self.campo_cliente.text().strip()
        )

        correo = (
            self.campo_correo.text().strip()
        )

        nit = (
            self.campo_nit.text().strip()
        )

        direccion = (
            self.campo_direccion.text().strip()
        )

        producto = (
            self.campo_producto.text().strip()
        )

        cantidad = (
            self.campo_cantidad.text().strip()
        )

        precio = (
            self.campo_precio.text().strip()
        )


        if (
            not cliente
            or not nit
            or not direccion
            or not producto
            or not cantidad
            or not precio
        ):

            QMessageBox.warning(
                self,
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return None


        try:

            cantidad = int(
                cantidad
            )

            precio = float(
                precio
            )

        except ValueError:

            QMessageBox.warning(
                self,
                "Datos incorrectos",
                "La cantidad debe ser un número entero "
                "y el precio debe ser numérico."
            )

            return None


        if cantidad <= 0:

            QMessageBox.warning(
                self,
                "Cantidad incorrecta",
                "La cantidad debe ser mayor que cero."
            )

            return None


        if precio < 0:

            QMessageBox.warning(
                self,
                "Precio incorrecto",
                "El precio no puede ser negativo."
            )

            return None


        return (
            cliente,
            correo,
            nit,
            direccion,
            producto,
            cantidad,
            precio
        )


    def generar(self):

        datos = self.obtener_datos()

        if datos is None:
            return


        (
            cliente,
            correo,
            nit,
            direccion,
            producto,
            cantidad,
            precio
        ) = datos


        try:

            ruta = generar_cotizacion(
                cliente,
                nit,
                direccion,
                producto,
                cantidad,
                precio
            )


            QMessageBox.information(
                self,
                "Cotización generada",
                f"La cotización se generó correctamente.\n\n"
                f"Archivo:\n{ruta}"
            )


        except Exception as error:

            QMessageBox.critical(
                self,
                "Error",
                f"No fue posible generar la cotización.\n\n"
                f"Error: {error}"
            )


    def enviar_cotizacion(self):

        datos = self.obtener_datos()

        if datos is None:
            return


        (
            cliente,
            correo,
            nit,
            direccion,
            producto,
            cantidad,
            precio
        ) = datos


        # --------------------------------------------------
        # Validar correo
        # --------------------------------------------------

        if not correo:

            QMessageBox.warning(
                self,
                "Correo requerido",
                "Debe ingresar el correo electrónico "
                "del cliente."
            )

            self.campo_correo.setFocus()

            return


        if "@" not in correo or "." not in correo:

            QMessageBox.warning(
                self,
                "Correo incorrecto",
                "Ingrese un correo electrónico válido."
            )

            self.campo_correo.setFocus()

            return


        try:

            # --------------------------------------------------
            # Generar primero la cotización
            # --------------------------------------------------

            ruta = generar_cotizacion(
                cliente,
                nit,
                direccion,
                producto,
                cantidad,
                precio
            )


            # --------------------------------------------------
            # Enviar por Gmail API
            # --------------------------------------------------

            id_mensaje = enviar_correo(
                destinatario=correo,
                asunto=f"Cotización para {cliente}",
                mensaje=f"""
Estimado/a {cliente}:

Adjunto encontrará la cotización solicitada.

Producto: {producto}
Cantidad: {cantidad}
Precio unitario: Q{precio:.2f}
Total: Q{cantidad * precio:.2f}

Gracias por su preferencia.

Saludos cordiales.
Sistema de Gestión
""",
                archivo_adjunto=ruta
            )


            QMessageBox.information(
                self,
                "Cotización enviada",
                f"La cotización fue generada y enviada "
                f"correctamente.\n\n"
                f"Destinatario:\n{correo}\n\n"
                f"Archivo:\n{ruta}\n\n"
                f"ID del mensaje:\n{id_mensaje}"
            )


        except Exception as error:

            QMessageBox.critical(
                self,
                "Error al enviar",
                f"No fue posible enviar la cotización.\n\n"
                f"Error:\n{error}"
            )


    def limpiar(self):

        self.campo_cliente.clear()

        self.campo_correo.clear()

        self.campo_nit.clear()

        self.campo_direccion.clear()

        self.campo_producto.clear()

        self.campo_cantidad.clear()

        self.campo_precio.clear()

        self.campo_cliente.setFocus()