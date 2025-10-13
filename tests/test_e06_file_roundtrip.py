# tests/test_e06_file_roundtrip.py

import pytest
from src.files import save_lines, load_lines
def test_save_and_load_lines(tmp_path):
    """Guardar y leer una lista, comprobando que se recupera igual"""
    archivo = tmp_path / "archivo.txt"
    datos = ["uno", "dos", "tres"]
    
    save_lines(lines= datos, path= archivo)
    
    resultado = load_lines(archivo)

    assert resultado == datos

def test_empty_file_returns_empty_lines(tmp_path):
    """Un archivo vacío devuelve una lista vacía"""
    archivo = tmp_path / "archivo_vacio.txt"
    archivo.write_text("")

    resultado = load_lines(archivo)

    assert resultado == []
