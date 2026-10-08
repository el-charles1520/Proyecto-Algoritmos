"""
PROYECTO ALGORITMOS
Sistema de Gestión de Inventario y Ventas

Archivo principal del programa.
"""

import sys

from PyQt5.QtWidgets import QApplication

from interfaz.menu import VentanaPrincipal


def main():
    """Inicia la aplicación."""

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()