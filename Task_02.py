#  Практическое задание к уроку № 2 (Циклы. Рекурсия. Функции.)

#  2. Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# решение с числом в виде str
number = input('Введите число: ')
even = 0
odd = 0
for k in number:
    num = int(k)
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {number}: четных цифр - {even}, нечетных - {odd} ')

# решение с числом в виде int
number = int(input('Введите число: '))
even = 0
odd = 0
while number > 0:
    if (number % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10
print(f'четных цифр - {even}, нечетных - {odd} ')


#  3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)


# решение с числом в виде int
number = int(input('Введите число: '))
m = 0  # перевернутое число
while number > 0:
    m = m * 10 + number % 10
    number //= 10
print(m)


# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


last_num = int(input('ведите конечное число ряда: '))
x = 1  # первое число ряда
sum = 1
lst = [1]  # ряд чисел
while last_num > 1:  # 1 т.к. первый элемент уже присутствует в списке
    x = - x / 2  # характеристика списка
    lst.append(x)
    sum += x
    last_num -= 1
print(f'Сумма элементов списка: {lst}\n{sum}')


#  7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
#  выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
user_num = int(input('ведите последнее число ряда: '))


def first(num1):
    sum_num = 0
    for i in range(1, num1 + 1):
        sum_num += i
    return sum_num


def second(num2):
    return num2 * (num2 + 1) / 2


while user_num > 0:
    if first(user_num) == second(user_num):
        print(f'Для n={user_num} - True')
    else:
        print(f'Для n={user_num} - False')
        break
    user_num -= 1


''' Вариант с выборочным одиночным сравнением '''

last_num = int(input('ведите число: '))
sum_num = 0
for i in range(1, last_num + 1):
    sum_num += i
equation = last_num * (last_num + 1) / 2
if sum_num == equation:
    print('равенство выполняется')
else:
    print('равенство не выполняется')
print(f'сумма ряда чисел: {sum_num}')
print(f'результат формулы: {equation}')


# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

user_range = input('Введите последовательность чисел: ')
user_like = input('Введите цифру для поиска: ')
count = 0
for i in user_range:
    if i == user_like:
        count += 1
print(f'Цифра {user_like} встречается в последовательности {user_range}: {count} раз(а)')


# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

''' использование числа '''
n1 = int(input('первое число: '))
n2 = int(input('второе число: '))

def sum_numbers(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if sum_numbers(n1) > sum_numbers(n2):
    print(f'У числа {n1} была наибольшая сумма цифр: {sum_numbers(n1)}')
else:
    print(f'У числа {n2} была наибольшая сумма цифр: {sum_numbers(n2)}')


''' использование строки'''
# определение суммы многозначного числа
def sum_numbers(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum

user_num = input('Введите многозначные числа разделенные пробелом: ')
list_number = [i for i in user_num.split()]

max_number = 0
max_sum = 0
for i in list_number:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'У числа {max_number} была наибольшая сумма цифр: {max_sum}')


# Дополнительное задание (344. Reverse String (from LeetCode))
# Перевернутая строка
# Напишите функцию, которая переворачивает строку. Входная строка задается как массив символов.
#   С помощью рекурсии

def reverse_string(user_string):
    if user_string == "":
        return user_string
    else:
        # передаем заново в функцию 'reverse_string' строку без первого символа
        #  и путем конкатенации поочередно склеиваем первые символы с строку "наоборот"
        return reverse_string(user_string[1:]) + user_string[:1]


a = reverse_string('reverse abba')
print(a)


# Дополнительное задание (231. Power of Two (from LeetCode))
# Подается целое число  'n', вернуть true, если оно является степенью двойки. В противном случае вернуть ложь.
# (Целое число  'n' является степенью двойки, если существует целое число x такое, что n == 2**x)
#   С помощью рекурсии:


def is_power_2(num):
    if num == 1:
        return print(True)
    elif 1 > num < 2:
        return print(False)
    else:
        return is_power_2(num / 2)


print(is_power_2(16))


# Цикл while
n = int(input('введите число: '))
i = 1
while i < n:
    i *= 2
if i == n:
    print(True)
else:
    print(False)


# Использование побитового сдвига


def is_power_two(b):
    return b and (not (b & (b - 1)))  # для числа степени двойки выражение b & (b - 1) всегда дает '0' (False)


num1 = 4
print(is_power_two(num1))
