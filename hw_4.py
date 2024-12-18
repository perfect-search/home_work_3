import os
import sys
from pathlib import Path
from colorama import Fore, Style, init

init()


def total_salary(path: str) -> tuple:
    total_salary = 0
    count_employees = 0

    try:
        current_file_path = Path(path)

        with open(current_file_path, 'r', encoding='utf-8') as c_f:
            for line in c_f:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count_employees += 1

        average_salary = total_salary / count_employees
        return (int(total_salary), float(average_salary))

    except FileNotFoundError:
        print(f"Файл {current_file_path} не найден.")
        return None
    except ValueError:
        print("Ошибка в формате файла.")
        return None
    except Exception as e:
        print(e)


print(type(total_salary('fff.txt')))


def get_cats_info(path: str) -> dict:
    cats_list = []

    try:
        current_file_path = Path(path)

        with open(current_file_path, 'r', encoding='utf-8') as c_f:
            for line in c_f:
                id, name, age = line.strip().split(',')
                cats_list.append({'id': id, 'name': name, 'age': int(age)})

        return cats_list

    except FileNotFoundError:
        print(f"Файл {current_file_path} не найден.")
        return None
    except ValueError:
        print("Ошибка в формате файла.")
        return None
    except Exception as e:
        print(e)


print(get_cats_info('cats.txt'))


def print_directory_structure(path: str):
    try:
        for root, dirs, files in os.walk(path):
            print(f"{Fore.BLUE}{root}{Style.RESET_ALL}")
            for dir in dirs:
                print(f"  {Fore.GREEN}{dir}{Style.RESET_ALL}")
            for file in files:
                print(f"  {Fore.YELLOW}{file}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"Директория {path} не найдена.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Неправельное количество аргументов. Введите путь к директории.")
        sys.exit(1)

    directory_path = sys.argv[1]
    print_directory_structure(directory_path)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def replace_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Phone replaced."


def get_contact_user(args, contacts):
    name = str(args)
    return contacts[name]


def get_all_numbers(contacts):
    for value in contacts.values():
        return value


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(replace_phone(args, contacts))
        elif command == "phone":
            print(get_contact_user(args, contacts))
        elif command == "all":
            print(get_all_numbers(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
