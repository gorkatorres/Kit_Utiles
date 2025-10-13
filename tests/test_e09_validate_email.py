# tests/test_e09_validate_email.py

import pytest
from src.strings import validate_email

# Emails válidos
@pytest.mark.parametrize("email", [
    "user@example.com",
    "nombre.apellido@dominio-es.org",
    "u_1-2@dominio.net"
])
def test_validate_email_valid(email):
    """Emails válidos deben devolver True"""
    assert validate_email(email) is True

# Emails inválidos
@pytest.mark.parametrize("email", [
    "sin_arroba.com",
    "user@dominio.",
    "user@dominio.c",
    "@dominio.com",
    "user@.com",
    "user@@dominio.com",
    "user dominio@dominio.com"
])
def test_validate_email_invalid(email):
    """Emails inválidos deben devolver False"""
    assert validate_email(email) is False
