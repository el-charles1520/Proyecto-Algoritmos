import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


from interfaz.pedidos import VentanaPedidos


app = QApplication(sys.argv)

ventana = VentanaPedidos()

ventana.show()

sys.exit(app.exec_())