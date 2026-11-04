import pytest
from .code import is_adult

# 1. Тестируем корректные граничные значения (позитивные тесты)
@pytest.mark.parametrize("age, expected", [
    (18, True),   # Точная нижняя граница (включительно)
    (19, True),   # Чуть выше нижней границы
    (119, True),  # Чуть ниже верхней границы
    (120, True),  # Точная верхняя граница (включительно)
])
def test_is_adult_boundaries_valid(age, expected):
    assert is_adult(age) == expected


# 2. Тестируем значения за рамками границ (негативные тесты)
@pytest.mark.parametrize("age, expected", [
    (17, False),  # Чуть ниже нижней границы (не входит)
    (0, False),   # Далеко за пределами нижнего диапазона
    (121, False), # Чуть выше верхней границы (не входит)
])
def test_is_adult_boundaries_invalid(age, expected):
    assert is_adult(age) == expected


# 3. Экстремальные и специальные значения
def test_is_adult_negative_age():
    assert is_adult(-1) is False

def test_is_adult_invalid_type():
    with pytest.raises(TypeError):
        is_adult("18")  # Граничное условие по типу данных