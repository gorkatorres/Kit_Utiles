import pytest
from src.numbers import sum_list
<<<<<<< HEAD
<<<<<<< HEAD
# Hola, este es un comentario de ejemplo.
=======
#esta linea no la tienes
>>>>>>> a9927ee (	modified:   tests/test_e01_sum_list.py)
=======
# Hola este es un comentario de ejemplo
>>>>>>> e24726f (	modified:   tests/__pycache__/test_e01_sum_list.cpython-311-pytest-8.4.2.pyc)

def test_sum_list():
    """Prueba que la suma de [1, 2, 3, 4] sea 10"""
    lista = [1, 2, 3, 4]
    resultado = sum_list(lista)
    assert resultado == 10, f"Se esperaba 10, pero se obtuvo {resultado}"

def test_sum_list_vacia():
    """Prueba que una lista vacía devuelva 0"""
    lista = []
    resultado = sum(lista)
    assert resultado == 0, f"Se esperaba 0, pero se obtuvo {resultado}"
