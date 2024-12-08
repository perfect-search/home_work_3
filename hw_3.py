from datetime import datetime
import random
import re


def get_days_from_today(date: str) -> int:
    rezult = 0

    try:
        date_today = datetime.now()
        date_comparison = datetime.strptime(date, "%Y-%m-%d")
        rezult = date_today.date() - date_comparison.date()
        rezult = rezult.days
    except Exception as e:
        print(e)

    return rezult


print(get_days_from_today('2022-12-03'))


def get_numbers_ticket(min_num, max_num, quantity):
    result_list = []

    try:
        if (min_num >= 1 and max_num < 1001 and quantity < 999):
            i = 0
            sett = set()
            while len(sett) < quantity:
                sett.add(random.randrange(min_num, max_num))
                i += 1
            
            result_list = sorted(list(sett))
        
    except Exception as e:
        print(e)

    return result_list


print(get_numbers_ticket(1, 49, 6))


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

    if (cleaned_number[0] != '+'):
        if(cleaned_number[0] == '3'):
            cleaned_number = f'+{cleaned_number}'
        elif (cleaned_number[0] == '0'):
            cleaned_number = f'+38{cleaned_number}'

    return cleaned_number


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
