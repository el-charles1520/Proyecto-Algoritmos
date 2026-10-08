"""
Funciones para enviar correos mediante Gmail API.
"""

from pathlib import Path
import base64

from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


# ==========================================================
# RUTAS
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

ARCHIVO_TOKEN = (
    CARPETA_PROYECTO /
    "token.json"
)


# ==========================================================
# CONFIGURACIÓN DE GMAIL
# ==========================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]


# ==========================================================
# FUNCIÓN PARA ENVIAR CORREO
# ==========================================================

def enviar_correo(
    destinatario,
    asunto,
    mensaje,
    archivo_adjunto=None
):
    """
    Envía un correo utilizando Gmail API.

    Parámetros:
        destinatario: correo electrónico del destinatario.
        asunto: asunto del correo.
        mensaje: contenido del correo.
        archivo_adjunto: archivo opcional que se enviará
                         como adjunto.

    Retorna:
        ID del mensaje enviado.
    """

    # ------------------------------------------------------
    # Verificar token
    # ------------------------------------------------------

    if not ARCHIVO_TOKEN.exists():

        raise FileNotFoundError(
            "No se encontró token.json. "
            "Debe realizarse primero la autenticación "
            "con Gmail API."
        )


    # ------------------------------------------------------
    # Cargar credenciales
    # ------------------------------------------------------

    credenciales = (
        Credentials.from_authorized_user_file(
            ARCHIVO_TOKEN,
            SCOPES
        )
    )


    # ------------------------------------------------------
    # Crear servicio Gmail
    # ------------------------------------------------------

    servicio = build(
        "gmail",
        "v1",
        credentials=credenciales
    )


    # ------------------------------------------------------
    # Crear mensaje
    # ------------------------------------------------------

    correo = EmailMessage()

    correo["To"] = destinatario
    correo["Subject"] = asunto

    correo.set_content(
        mensaje
    )


    # ------------------------------------------------------
    # Adjuntar archivo
    # ------------------------------------------------------

    if archivo_adjunto is not None:

        ruta_archivo = Path(
            archivo_adjunto
        )

        if not ruta_archivo.exists():

            raise FileNotFoundError(
                f"No se encontró el archivo adjunto: "
                f"{ruta_archivo}"
            )


        with open(
            ruta_archivo,
            "rb"
        ) as archivo:

            contenido = archivo.read()


        # --------------------------------------------------
        # Detectar tipo de archivo
        # --------------------------------------------------

        extension = (
            ruta_archivo.suffix.lower()
        )


        if extension == ".docx":

            maintype = "application"

            subtype = (
                "vnd.openxmlformats-officedocument"
                ".wordprocessingml.document"
            )

        elif extension == ".pdf":

            maintype = "application"

            subtype = "pdf"

        else:

            maintype = "application"

            subtype = "octet-stream"


        # --------------------------------------------------
        # Agregar archivo
        # --------------------------------------------------

        correo.add_attachment(
            contenido,
            maintype=maintype,
            subtype=subtype,
            filename=ruta_archivo.name
        )


    # ------------------------------------------------------
    # Codificar mensaje
    # ------------------------------------------------------

    mensaje_codificado = (
        base64.urlsafe_b64encode(
            correo.as_bytes()
        ).decode()
    )


    cuerpo = {
        "raw": mensaje_codificado
    }


    # ------------------------------------------------------
    # Enviar correo
    # ------------------------------------------------------

    resultado = (
        servicio.users()
        .messages()
        .send(
            userId="me",
            body=cuerpo
        )
        .execute()
    )


    return resultado["id"]