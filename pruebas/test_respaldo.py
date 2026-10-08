import sys
from pathlib import Path


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


from funciones.respaldo import crear_respaldo


ruta = crear_respaldo()


if ruta is not None:

    print(
        "RESPALDO CREADO CORRECTAMENTE"
    )

    print(
        f"Archivo creado en: {ruta}"
    )

else:

    print(
        "NO SE PUDO CREAR EL RESPALDO"
    )