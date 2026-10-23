from pathlib import Path
import openpyxl

BASE_DIR = Path(__file__).resolve().parent.parent
archivo = BASE_DIR / "datos" / "Inventario.xlsx"

if archivo.exists():
    print(f"archivo encontrado en {archivo.resolve()}")
else:
    print("archivo no encontrado")
    
libro = openpyxl.load_workbook(archivo)