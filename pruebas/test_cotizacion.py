import sys
from pathlib import Path


CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


from funciones.cotizacion import generar_cotizacion


ruta = generar_cotizacion(
    "Juan Pérez",
    "123456-8",
    "Jalapa Centro",
    "Mouse",
    2,
    100
)


print("COTIZACIÓN GENERADA CORRECTAMENTE")

print(
    f"Archivo creado en: {ruta}"
)