import math

def calc_expression(x, y):
    if x <= 0:
        return "Помилка: x має бути більшим за 0 (ОДЗ для логарифма)."

    result = math.log(x) + math.cos(y)
    return round(result, 4)
