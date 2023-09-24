# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


# Проверка
# num = int(input())
# hex_num = hex(num)
# print(hex_num)

num = int(input("Введите десятичное число: "))
number_system = "0123456789ABCDEF"
hexadecimal_system = ""

while num > 0:
    remainder = num % 16
    hexadecimal_digit = number_system[remainder]
    hexadecimal_system = hexadecimal_digit + hexadecimal_system
    num //= 16

print("Шестнадцатеричное число:", hexadecimal_system)