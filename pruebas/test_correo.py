import sys
from pathlib import Path


CARPETA_PROYECTO = Path(
    __file__
).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


from funciones.correo import enviar_correo


CORREO_REMITENTE = "carlosvaldez0518@gmail.com"

CONTRASENA_APLICACION = "proyecto"

CORREO_DESTINATARIO = "carlosvaldeze842zyk.experiment@gmail.com"


CARPETA_DOCUMENTOS = (
    CARPETA_PROYECTO
    / "documentos"
)


# Buscar automáticamente el archivo de cotización
archivos = list(
    CARPETA_DOCUMENTOS.glob(
        "Cotizacion_*.docx"
    )
)


if not archivos:

    print(
        "NO SE ENCONTRO NINGUNA COTIZACION."
    )

    sys.exit()


ARCHIVO = archivos[0]


resultado, mensaje = enviar_correo(
    CORREO_REMITENTE,
    CONTRASENA_APLICACION,
    CORREO_DESTINATARIO,
    "Cotizacion",
    "Se adjunta la cotizacion solicitada.",
    ARCHIVO
)


print(
    mensaje
)