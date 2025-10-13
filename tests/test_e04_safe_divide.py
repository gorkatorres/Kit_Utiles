
import pytest
from src.numbers import safe_divide

def test_division():
    """Comprueba que 10 / 2 devuelve 5"""
    assert safe_divide(10, 2) == 5

def test_division_por_cero():
    """Comprueba que dividir entre 0 lanza ValueError"""
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(10, 0)

def test_division_erroneo():
    """Comprueba que pasar un string como primer argumento lanza TypeError"""
    with pytest.raises(TypeError):
        safe_divide("3", 1)
