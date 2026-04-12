"""
МОДУЛЬ 1: ПРОСТЫЕ ТИПЫ ДАННЫХ В PYTHON
"""

# ==================== ЧАСТЬ 1: ТЕОРИЯ И ПРИМЕРЫ ====================

print("\n" + "="*60)
print("ЧАСТЬ 1: ТЕОРИЯ И ПРИМЕРЫ")
print("="*60 + "\n")

# ---------- 1. int (целые числа) ----------
print("1. ТИП int - целые числа")
age = 25
students_count = -3
big_number = 1_000_000  # подчеркивания для удобства чтения

print(f"age = {age}, тип: {type(age)}")
print(f"students_count = {students_count}, тип: {type(students_count)}")
print(f"big_number = {big_number}, тип: {type(big_number)}")
print(f"age + 5 = {age + 5}\n")

# ---------- 2. float (числа с плавающей точкой) ----------
print("2. ТИП float - числа с плавающей точкой")
pi = 3.14159
temperature = -2.5

print(f"pi = {pi}, тип: {type(pi)}")
print(f"temperature = {temperature}, тип: {type(temperature)}")
print(f"pi * 2 = {pi * 2}")

# Проблема float
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004
print("⚠️ ВНИМАНИЕ: float неточен для финансовых расчетов!\n")

# ---------- 3. str (строки) ----------
print("3. ТИП str - строки")
name = "Анна"
message = 'Привет, мир!'
multi_line = """Это
несколько
строк"""

print(f"name = {name}, тип: {type(name)}")
print(f"message = {message}, тип: {type(message)}")
print(f"Конкатенация: {name + ' ' + message}")
print(f"f-строка: Меня зовут {name}\n")

# ---------- 4. bool (логический тип) ----------
print("4. ТИП bool - логический тип")
is_student = True
has_job = False

print(f"is_student = {is_student}, тип: {type(is_student)}")
print(f"has_job = {has_job}, тип: {type(has_job)}")
print(f"5 > 3 = {5 > 3}")
print(f"10 == 11 = {10 == 11}\n")

# ---------- 5. None (отсутствие значения) ----------
print("5. ТИП None - отсутствие значения")
result = None
user_address = None

print(f"result = {result}, тип: {type(result)}")
print("None используется когда значение еще неизвестно или отсутствует\n")

# ---------- 6. Decimal (точные десятичные дроби) ----------
print("6. ТИП Decimal - точные десятичные дроби")
from decimal import Decimal

price = Decimal('19.99')
tax = Decimal('0.07')
total = price + (price * tax)

print(f"price = {price}, тип: {type(price)}")
print(f"tax = {tax}")
print(f"total = {total}")
print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")
print("✅ Decimal решает проблему неточности float!\n")

# ---------- 7. timestamp (момент времени) ----------
print("7. ТИП timestamp - момент времени")
import time
from datetime import datetime

now = time.time()  # текущий timestamp
print(f"Текущий timestamp: {now}")
print(f"Тип timestamp: {type(now)}")  # timestamp - это float

# Превращаем timestamp в читаемый вид
readable = time.ctime(now)
print(f"Читаемый формат: {readable}")

# Более красивый формат
dt = datetime.fromtimestamp(now)
print(f"Формат ISO: {dt.strftime('%Y-%m-%d %H:%M:%S')}\n")

# ==================== ЧАСТЬ 2: ЗАДАНИЯ ДЛЯ САМОПРОВЕРКИ ====================

print("\n" + "="*60)
print("ЧАСТЬ 2: ЗАДАНИЯ ДЛЯ САМОПРОВЕРКИ (устно)")
print("="*60 + "\n")

print("Вопросы для размышления:")
print("1. Какой тип данных у 100, 100.0, '100'?")
print("2. Что выведет print(0.3 == 0.1 + 0.2) и почему?")
print("3. Как правильно сложить Decimal('0.1') и Decimal('0.2')?")
print("4. Что означает None? Приведи пример использования.")
print("5. Как получить текущий timestamp и перевести его в строку?")
print("\nОтветы найдешь в коде выше и в домашнем задании.\n")
