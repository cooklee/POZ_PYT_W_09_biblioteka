def add(a, b):
    if a < 0 or b < 0:
        raise ValueError('Babol')
    if a == 5:
        return "Dupa"
    return a + b


from datetime import datetime
from random import randint


def div(a, b):
    return a / b


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "female" if int(pesel[-2]) % 2 == 0 else "male"
    year = pesel[0:2]
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    if month < 20:
        year_start = '19'
    elif month < 40:
        year_start = '20'
        month -= 20
    elif month < 60:
        year_start = '21'
        month -= 40
    elif month < 80:
        year_start = '18'
        month -= 60
    year = int(year_start+year)
    birth_date = datetime(year, month, day)
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result
