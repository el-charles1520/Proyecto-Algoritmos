import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CARPETA_PROYECTO))


from interfaz.clientes import VentanaClientes


app = QApplication(sys.argv)

ventana = VentanaClientes()

ventana.show()

sys.exit(app.exec_())