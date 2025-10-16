
from src.numbers import unique_sorted
#comentario3
def test_unique_sorted_numeros():
    """Comprueba que [3, 1, 2, 3, 2] devuelve [1, 2, 3]"""
    datos = [3, 1, 2, 3, 2]
    esperado = [1, 2, 3]
    assert unique_sorted(datos) == esperado

def test_unique_sorted_cadenas():
    """Comprueba que ["b", "a", "b"] devuelve ["a", "b"]"""
    datos = ["b", "a", "b"]
    esperado = ["a", "b"]
    assert unique_sorted(datos) == esperado
