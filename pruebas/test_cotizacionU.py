"""
Pruebas unitarias para las funciones de cotización.
"""

import sys
from pathlib import Path

from docx import Document


# ==========================================================
# AGREGAR LA CARPETA PRINCIPAL DEL PROYECTO
# ==========================================================

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

if str(CARPETA_PROYECTO) not in sys.path:
    sys.path.insert(0, str(CARPETA_PROYECTO))


# ==========================================================
# IMPORTAR FUNCIÓN
# ==========================================================

from funciones.cotizacion import generar_cotizacion


# ==========================================================
# PRUEBA 1 - GENERAR COTIZACIÓN
# ==========================================================

def test_generar_cotizacion():

    ruta = generar_cotizacion(
        "ClientePrueba",
        "000000-0",
        "Dirección de prueba",
        "Mouse",
        3,
        100
    )

    assert ruta is not None

    print(
        "✓ test_generar_cotizacion: CORRECTA"
    )


# ==========================================================
# PRUEBA 2 - VERIFICAR QUE EL ARCHIVO EXISTA
# ==========================================================

def test_archivo_cotizacion():

    ruta = generar_cotizacion(
        "ClientePrueba",
        "000000-0",
        "Dirección de prueba",
        "Mouse",
        3,
        100
    )

    assert Path(ruta).exists()

    print(
        "✓ test_archivo_cotizacion: CORRECTA"
    )


# ==========================================================
# PRUEBA 3 - VERIFICAR EXTENSIÓN
# ==========================================================

def test_extension_word():

    ruta = generar_cotizacion(
        "ClientePrueba",
        "000000-0",
        "Dirección de prueba",
        "Mouse",
        3,
        100
    )

    assert Path(ruta).suffix == ".docx"

    print(
        "✓ test_extension_word: CORRECTA"
    )


# ==========================================================
# PRUEBA 4 - VERIFICAR NOMBRE DEL ARCHIVO
# ==========================================================

def test_nombre_archivo():

    ruta = generar_cotizacion(
        "ClientePrueba",
        "000000-0",
        "Dirección de prueba",
        "Mouse",
        3,
        100
    )

    assert Path(ruta).name == (
        "Cotizacion_ClientePrueba.docx"
    )

    print(
        "✓ test_nombre_archivo: CORRECTA"
    )


# ==========================================================
# PRUEBA 5 - VERIFICAR CONTENIDO DEL WORD
# ==========================================================

def test_contenido_cotizacion():

    ruta = generar_cotizacion(
        "ClientePrueba",
        "000000-0",
        "Dirección de prueba",
        "Mouse",
        3,
        100
    )

    documento = Document(ruta)

    texto_completo = "\n".join(
        parrafo.text
        for parrafo in documento.paragraphs
    )

    assert "COTIZACIÓN" in texto_completo

    assert "Cliente: ClientePrueba" in texto_completo

    assert "NIT: 000000-0" in texto_completo

    assert "Dirección: Dirección de prueba" in texto_completo

    assert "TOTAL: Q300.00" in texto_completo

    print(
        "✓ test_contenido_cotizacion: CORRECTA"
    )


# ==========================================================
# EJECUTAR TODAS LAS PRUEBAS
# ==========================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("PRUEBAS UNITARIAS - COTIZACIÓN")
    print("=" * 55)
    print()

    test_generar_cotizacion()
    test_archivo_cotizacion()
    test_extension_word()
    test_nombre_archivo()
    test_contenido_cotizacion()

    print()
    print("=" * 55)
    print("TODAS LAS PRUEBAS DE COTIZACIÓN FUERON CORRECTAS")
    print("=" * 55)