# tests/test_e08_cli_sum.py

import pytest
from src.cli import main

def test_main_argumentos(capsys):
    """main(['prog', '1,2,3']) debe imprimir 6.0"""
    main(["prog", "1,2,3"])
    salida = capsys.readouterr().out.strip()
    assert salida == "6.0"

def test_main_sin_argumentos(capsys):
    """main(['prog']) debe imprimir 0"""
    main(["prog"])
    salida = capsys.readouterr().out.strip()
    assert salida == "0"
