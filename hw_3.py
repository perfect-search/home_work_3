from datetime import datetime
import random
import re


def get_days_from_today(date: str) -> int:

    date_today = datetime.now()
    rezult = 0

    if (len(date) == 10):
        if (date[4] == '-' and date[7] == '-'):
            date_comparison = datetime.strptime(date, "%Y-%m-%d")

            if (date_comparison.date() <= date_today.date()):
                rezult = date_today.date() - date_comparison.date()
                rezult = rezult.days
            else:
                print(f"Вы ввесли дату с будущего: {date}")

        else:
            print((
                f"Введите верный формат: 'YYYY-MM-DD'\n"
                f"Вы ввели: {date}\n"
            ))

    else:
        print((
            f"Вы ввели некорректную дату: {date}\n"
            f"Необходим формат 'YYYY-MM-DD'\n"
        ))

    return rezult


print(get_days_from_today('2022-12-03'))


def get_numbers_ticket(min, max, quantity):
    result_list = []

    if (min >= 1 and max < 1001 and quantity < 999):
        i = 0
        while i < quantity:
            result_list.append(random.randrange(min, max))
            i += 1

            if (result_list[0] == random.randrange(min, max)):
                continue

        return sorted(result_list)

    else:
        print((
            f"Неверные данные: min = {min}, max = {max}, quantity = {quantity}\n"
            f"Необходимы данные: min > 1, max <= 1000, quantity < 999\n"
        ))
        return result_list


print(get_numbers_ticket(1, 555, 3))


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)

    if(cleaned_number[0] != '+'):
        cleaned_number = f'+38{cleaned_number}'

    return cleaned_number



sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
