import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication


# Agregar la carpeta principal del proyecto
CARPETA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CARPETA_PROYECTO))


from interfaz.productos import VentanaProductos


app = QApplication(sys.argv)

ventana = VentanaProductos()

ventana.show()

sys.exit(app.exec_())