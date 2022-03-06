import pytest


def validate_length(password):
    return len(password) >= 7

def validate_upper(password):
    return any(x for x in password if x.isupper())

def validate_lower(password):
    return any(x for x in password if x.islower())

def validate_special(password):
    special = """!@#$%^&*()_+=-~{}[]:"|;'\<>?,./\|"""
    return any(x for x in password if x in special)

def validate_digit(password):
    return any(x for x in password if x.isdigit())

def validate_password(password):
    validators = [
        validate_digit,
        validate_special,
        validate_lower,
        validate_upper,
        validate_length
    ]
    for validator in validators:
        if not validator(password):
            return False
    return True

@pytest.mark.parametrize("password, result", [
    ("Aaaaa;1", True),
    ("Aa"*3, False),
    ("A"*7, False),
    ("a"*7, False),
    ("AaAaAaA", False),
    ("AaAaAa1", False),
])
def test_val_pass(password, result):
    assert validate_password(password) == result