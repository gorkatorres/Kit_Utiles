# tests/test_e10_grade.py

import pytest
from src.numbers import grade

# 1️⃣ Prueba parametrizada con valores límite
@pytest.mark.parametrize("score, expected", [
    (100, "A"), (90, "A"),
    (89, "B"), (80, "B"),
    (79, "C"), (70, "C"),
    (69, "D"), (60, "D"),
    (59, "F"), (0, "F")
])
def test_grade_valid(score, expected):
    """Comprueba las calificaciones según los límites"""
    assert grade(score) == expected

# 2️⃣ Prueba para valores fuera de rango
@pytest.mark.parametrize("score", [-1, 101])
def test_grade_out_of_range(score):
    """Valores fuera de 0-100 deben lanzar ValueError"""
    with pytest.raises(ValueError):
        grade(score)

# 3️⃣ Prueba donde score no sea entero
def test_grade_not_integer():
    """Valores no enteros deben lanzar TypeError"""
    with pytest.raises(TypeError):
        grade(85.0)
