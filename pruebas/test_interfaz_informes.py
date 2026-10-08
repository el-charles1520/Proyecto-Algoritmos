import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


from interfaz.informes import VentanaInformes


app = QApplication(sys.argv)

ventana = VentanaInformes()

ventana.show()

sys.exit(app.exec_())