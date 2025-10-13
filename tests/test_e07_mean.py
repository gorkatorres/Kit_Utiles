
import pytest
from src.numbers import mean
def test_mean():
    """La media de [1, 2, 3, 4] debe ser 2.5"""
    datos = [1, 2, 3, 4]
    resultado = mean(datos)
    assert resultado == 2.5

def test_mean_vacia():
    """Una lista vacía debe lanzar ValueError("empty sequence")"""
    datos = []
    with pytest.raises(ValueError, match="empty sequence"):
        mean(datos)
