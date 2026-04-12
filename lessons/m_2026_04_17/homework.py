"""
- Повторить пройденный материал
- Изучить
-- Что такое тип данных и зачем он нужен.
-- Числа: целые (int) и дробные (float).
-- Строки (str) и работа с кавычками.
-- Логический тип (bool): правда и ложь.
-- Пустой тип (None) — обозначение «ничего».
-- Decimal — точные деньги (важно для финансов).
-- timestamp — как компьютер хранит время.
- Изучить материал из файла lessons/m_2026_04_17/info.py
- Решить задачи из данного файла (в этом же файле)
- Подготовить вопросы
"""

from decimal import Decimal


# ==================== ЧАСТЬ 3: ДОМАШНЕЕ ЗАДАНИЕ ====================

print("\n" + "="*60)
print("ЧАСТЬ 3: ДОМАШНЕЕ ЗАДАНИЕ")
print("="*60 + "\n")

# ---------- ЗАДАЧА 1 (легкая) ----------
print("ЗАДАЧА 1: Объявление переменных и их типы")
print("-" * 40)

# ТВОЙ КОД:
items = 10
price_per_item = 5.99
product_name = "Книга"
is_available = True
discount = None

# Выводим типы
print(f"items = {items}, тип: {type(items)}")
print(f"price_per_item = {price_per_item}, тип: {type(price_per_item)}")
print(f"product_name = {product_name}, тип: {type(product_name)}")
print(f"is_available = {is_available}, тип: {type(is_available)}")
print(f"discount = {discount}, тип: {type(discount)}")
print("\n")

# ---------- ЗАДАЧА 2 (проблема float) ----------
print("ЗАДАЧА 2: Сравнение float и Decimal")
print("-" * 40)

# ТВОЙ КОД:
float_result = 0.1 + 0.2
decimal_result = Decimal('0.1') + Decimal('0.2')

print(f"float: 0.1 + 0.2 = {float_result}")
print(f"Decimal: 0.1 + 0.2 = {decimal_result}")
print(f"Результаты равны? {float_result == decimal_result}")
print("\n💡 ОТВЕТ: float использует двоичную систему и не может точно")
print("представить 0.1 и 0.2. Decimal предназначен для точных")
print("десятичных вычислений, поэтому результат точный.\n")

# ---------- ЗАДАЧА 3 (работа со строками) ----------
print("ЗАДАЧА 3: Работа со строками")
print("-" * 40)

# ТВОЙ КОД:
city = "San Francisco"

print(f"Исходная строка: '{city}'")
print(f"Первая буква: '{city[0]}'")
print(f"Последняя буква: '{city[-1]}'")
print(f"f-строка: Я живу в городе {city}\n")

# ---------- ЗАДАЧА 4 (timestamp) ----------
print("ЗАДАЧА 4: Работа с timestamp")
print("-" * 40)

# ТВОЙ КОД:
from datetime import datetime
import time

# Получаем текущий timestamp
current_ts = time.time()
print(f"Текущий timestamp: {current_ts}")

# Переводим в читаемый формат
dt_object = datetime.fromtimestamp(current_ts)
formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
print(f"Читаемый формат: {formatted_time}\n")
