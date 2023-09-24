# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

fraction1 = input('Введите первую дробь через /: ')
fraction2 = input('Введите вторую дробь через /: ')

numerator_1_fraction1 = int(fraction1.split('/')[0])
denominator_1_fraction1 = int(fraction1.split('/')[1])
numerator_2_fraction2 = int(fraction2.split('/')[0])
denominator_2_fraction2 = int(fraction2.split('/')[1])

# Сложение дробей

if denominator_1_fraction1 != denominator_2_fraction2:
    common_numerator = (numerator_1_fraction1 * denominator_2_fraction2) + (numerator_2_fraction2 * denominator_1_fraction1)
    common_denominator = denominator_1_fraction1 * denominator_2_fraction2
else:
    common_numerator = numerator_1_fraction1 + numerator_2_fraction2
    common_denominator = denominator_1_fraction1
    print(f'{common_numerator}/{common_denominator}')

# Произведение дробей
product_of_numerators = numerator_1_fraction1 * numerator_2_fraction2
product_of_divisors = denominator_1_fraction1 * denominator_2_fraction2

# Сокращение

for i in range(2, common_numerator + 1):
    while common_numerator % i == 0 and common_denominator % i ==0:
        common_numerator //= i
        common_denominator //= i

for i in range(2, product_of_numerators + 1):
    while product_of_numerators % i == 0 and product_of_divisors % i ==0:
        product_of_numerators //= i
        product_of_divisors //= i

print(f'Сложение дробей {fraction1} и {fraction2} = {common_numerator}/{common_denominator}')
print(f'Произведение дробей {fraction1} и {fraction2} = {product_of_numerators}/{product_of_divisors}')