"""
Prueba de la función de envío de correo mediante Gmail API.
"""

from pathlib import Path
import sys


# ==========================================================
# UBICAR LA CARPETA PRINCIPAL DEL PROYECTO
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(CARPETA_PROYECTO)
)


# ==========================================================
# IMPORTAR FUNCIÓN
# ==========================================================

from funciones.correo import enviar_correo


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ARCHIVO_COTIZACION = (
    CARPETA_PROYECTO /
    "documentos" /
    "Cotizacion_Juan Pérez.docx"
)

DESTINATARIO = "carlosvaldez0518@gmail.com"


# ==========================================================
# PRUEBA
# ==========================================================

def probar_envio():

    print()
    print("========================================")
    print("PRUEBA DE ENVÍO DE CORREO")
    print("========================================")
    print()

    print("Destinatario:")
    print(DESTINATARIO)

    print()

    print("Archivo:")
    print(ARCHIVO_COTIZACION)

    print()

    try:

        id_mensaje = enviar_correo(
            destinatario=DESTINATARIO,
            asunto="Prueba de envío - Sistema de Gestión",
            mensaje="""
Estimado cliente:

Este es un correo de prueba enviado
automáticamente mediante Gmail API.

Se adjunta una cotización en formato Word.

Saludos cordiales.
Sistema de Gestión
""",
            archivo_adjunto=ARCHIVO_COTIZACION
        )

        print(
            "========================================"
        )

        print(
            "CORREO ENVIADO CORRECTAMENTE"
        )

        print(
            "========================================"
        )

        print()

        print("ID del mensaje:")
        print(id_mensaje)

        print()

        print(
            "La función funciones/correo.py"
        )

        print(
            "funciona correctamente."
        )

        print()

    except Exception as error:

        print()
        print(
            "========================================"
        )

        print(
            "ERROR AL ENVIAR EL CORREO"
        )

        print(
            "========================================"
        )

        print()

        print(error)

        print()


# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":

    probar_envio()