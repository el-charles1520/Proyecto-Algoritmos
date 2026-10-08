"""
Pruebas unitarias para la función de correo.
"""

import sys
from pathlib import Path


# ==========================================================
# AGREGAR LA CARPETA PRINCIPAL DEL PROYECTO
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

if str(CARPETA_PROYECTO) not in sys.path:
    sys.path.insert(0, str(CARPETA_PROYECTO))


# ==========================================================
# IMPORTAR FUNCIÓN
# ==========================================================

from funciones.correo import enviar_correo


# ==========================================================
# EJECUTAR PRUEBA
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBA UNITARIA - CORREO")
    print("=" * 55)
    print()

    try:

        id_mensaje = enviar_correo(

            destinatario="jenniferjimenez1615@gmail.com",

            asunto="Prueba del sistema de gestión",

            mensaje="""
Este es un correo de prueba generado
desde el sistema de gestión.

La prueba de la función de correo
se realizó correctamente.
"""
        )

        assert id_mensaje is not None

        assert len(id_mensaje) > 0

        print(
            "✓ test_enviar_correo: CORRECTA"
        )

        print()
        print(
            f"ID del mensaje enviado: {id_mensaje}"
        )

        print()
        print("=" * 55)
        print("LA PRUEBA DE CORREO FUE CORRECTA")
        print("=" * 55)

    except Exception as error:

        print()
        print(
            "✗ test_enviar_correo: ERROR"
        )

        print()
        print(
            f"Error: {error}"
        )