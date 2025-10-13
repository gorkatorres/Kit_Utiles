# tests/test_e05_word_count.py

import pytest
from src.strings import word_count
@pytest.fixture
def texto():
    """Devuelve el texto de prueba"""
    return "Hola, hola... ¿Qué tal? Tal vez bien: hola!"

def test_word_count(texto):
    """Verifica el conteo de palabras ignorando mayúsculas y signos de puntuación"""
    resultado = word_count(texto)
    
    assert resultado["hola"] == 3
    assert resultado["tal"] == 2
    assert resultado["qué"] == 1
    assert "inexistente" not in resultado
