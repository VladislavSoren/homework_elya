
def ticket_price(age):
    """
    - возраст меньше 0        -> "Неверный возраст"
    - от 0 до 6 включительно  -> 0
    - от 7 до 17 включительно -> 100
    - от 18 до 64 включительно -> 300
    - 65 и больше             -> 150
    """

    if type(age) != int:
        return "Введённые данные ошибочны"

    if age < 0:
        return "Неверный возраст"
    elif age <= 6:
        return "0"
    elif age <= 17:
        return "100"
    elif age <= 64:
        return "300"
    else:
        return "150"
