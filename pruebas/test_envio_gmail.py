"""
Prueba de envío de correo mediante Gmail API.
"""

from pathlib import Path
import base64

from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ARCHIVO_TOKEN = Path("token.json")

ARCHIVO_COTIZACION = (
    Path("documentos") /
    "Cotizacion_Juan Pérez.docx"
)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]


# ==========================================================
# DATOS DEL CORREO
# ==========================================================

DESTINATARIO = "carlosvaldez0518@gmail.com"

ASUNTO = "Cotización de producto"

MENSAJE = """
Estimado cliente:

Adjunto encontrará la cotización solicitada.

Gracias por su preferencia.

Saludos cordiales.
Sistema de Gestión
"""


# ==========================================================
# FUNCIÓN PARA ENVIAR EL CORREO
# ==========================================================

def enviar_correo():

    # ------------------------------------------------------
    # Verificar token
    # ------------------------------------------------------

    if not ARCHIVO_TOKEN.exists():

        print(
            "ERROR: No se encontró token.json"
        )

        return


    # ------------------------------------------------------
    # Verificar cotización
    # ------------------------------------------------------

    if not ARCHIVO_COTIZACION.exists():

        print(
            "ERROR: No se encontró la cotización:"
        )

        print(
            ARCHIVO_COTIZACION
        )

        return


    # ------------------------------------------------------
    # Cargar credenciales
    # ------------------------------------------------------

    credenciales = Credentials.from_authorized_user_file(
        ARCHIVO_TOKEN,
        SCOPES
    )


    # ------------------------------------------------------
    # Conectar con Gmail
    # ------------------------------------------------------

    servicio = build(
        "gmail",
        "v1",
        credentials=credenciales
    )


    # ------------------------------------------------------
    # Crear mensaje
    # ------------------------------------------------------

    mensaje = EmailMessage()

    mensaje["To"] = DESTINATARIO
    mensaje["Subject"] = ASUNTO

    mensaje.set_content(
        MENSAJE
    )


    # ------------------------------------------------------
    # Adjuntar cotización
    # ------------------------------------------------------

    with open(
        ARCHIVO_COTIZACION,
        "rb"
    ) as archivo:

        contenido = archivo.read()


    mensaje.add_attachment(
        contenido,
        maintype="application",
        subtype=(
            "vnd.openxmlformats-officedocument"
            ".wordprocessingml.document"
        ),
        filename="Cotizacion.docx"
    )


    # ------------------------------------------------------
    # Convertir mensaje a formato Gmail
    # ------------------------------------------------------

    mensaje_codificado = base64.urlsafe_b64encode(
        mensaje.as_bytes()
    ).decode()


    cuerpo = {
        "raw": mensaje_codificado
    }


    # ------------------------------------------------------
    # Enviar
    # ------------------------------------------------------

    resultado = servicio.users().messages().send(
        userId="me",
        body=cuerpo
    ).execute()


    # ------------------------------------------------------
    # Mostrar resultado
    # ------------------------------------------------------

    print()
    print("========================================")
    print("CORREO ENVIADO CORRECTAMENTE")
    print("========================================")
    print()
    print(
        "ID del mensaje:"
    )
    print(
        resultado["id"]
    )
    print()
    print(
        "Destinatario:"
    )
    print(
        DESTINATARIO
    )
    print()
    print(
        "Archivo adjunto:"
    )
    print(
        ARCHIVO_COTIZACION
    )
    print()


# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":

    try:

        enviar_correo()

    except Exception as error:

        print()
        print("========================================")
        print("ERROR AL ENVIAR EL CORREO")
        print("========================================")
        print()
        print(error)
        print()