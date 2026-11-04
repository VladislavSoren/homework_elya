"""
Правило порядка импорта:
- Сначала внутренние библиотеки Python: math, os, sys
- Внешние (установленные): pytest, requests
- Наши собственные модули: импорт из наших файлов
"""

#import math 

import pytest

from .main import ticket_price

@pytest.mark.parametrize("age, expected", [
    (-1, "Неверный возраст"),
    (1, "0"),
    (3, "0"),
    (6, "0"),
    (7, "100"),
    (10, "100"),
    (17, "100"),
    (18, "300"),
    (30, "300"),
    (64, "300"),
    (65, "150"),
    (80, "150"),
    ("18", "Введённые данные ошибочны"),
])
def test_ticket_price(age, expected):
    result = ticket_price(age)
    assert result == expected

# def test_ticket_price():
#     age = -1
#     result = ticket_price(age)
#     assert result == "Неверный возраст"

# def test_ticket_price():
#     with pytest.raises(TypeError):
#         ticket_price("18")  # Граничное условие по типу данных