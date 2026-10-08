"""
Prueba de autenticación con Gmail API.
"""

from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# ==========================================================
# RUTAS
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

CREDENTIALS_FILE = (
    CARPETA_PROYECTO /
    "credentials.json"
)

TOKEN_FILE = (
    CARPETA_PROYECTO /
    "token.json"
)


# ==========================================================
# PERMISOS
# ==========================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]


# ==========================================================
# AUTENTICACIÓN
# ==========================================================

def autenticar_gmail():

    if not CREDENTIALS_FILE.exists():

        print(
            "ERROR: No se encontró credentials.json"
        )

        print(
            CREDENTIALS_FILE
        )

        return


    print(
        "Iniciando autenticación con Gmail..."
    )

    print()


    flujo = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_FILE,
        SCOPES
    )


    credenciales = flujo.run_local_server(
        port=0
    )


    # ------------------------------------------------------
    # GUARDAR TOKEN
    # ------------------------------------------------------

    with open(
        TOKEN_FILE,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            credenciales.to_json()
        )


    # ------------------------------------------------------
    # CONECTAR CON GMAIL
    # ------------------------------------------------------

    servicio = build(
        "gmail",
        "v1",
        credentials=credenciales
    )


    print()
    print("========================================")
    print("AUTENTICACIÓN CORRECTA")
    print("========================================")
    print()
    print(
        "El programa se conectó correctamente"
    )
    print(
        "con Gmail API."
    )
    print()
    print(
        "El servicio de Gmail está listo."
    )
    print()
    print(
        "Token guardado en:"
    )
    print(
        TOKEN_FILE
    )
    print()


    return servicio


# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":

    autenticar_gmail()