# Puede fallar si la expresión regular no permite subdominios o TLD 2-10 letras.
from src.strings import validate_email
import re

def test_validate_email_subdominios_y_tld():
    ok = [
        "user@mail.example.com",
        "a_b.c-d@sub.domain.edu",
    ]
    ko = [
        "user@mail.example.c"      # TLD 1
        "user@mail.example.toolongtld" # TLD >10
        "user@@mail.com"
    ]
    for e in ok:
        assert validate_email(e)
    for e in ko:
        assert not validate_email(e)

def validate_email(email: str) -> bool:
    pattern = re.compile(
        r"^[a-zA-Z0-9_.+-]+@"                  
        r"(?:[a-zA-Z0-9-]+\.)+"                
        r"[a-zA-Z]{2,10}$"                     
    )
    return bool(pattern.match(email))