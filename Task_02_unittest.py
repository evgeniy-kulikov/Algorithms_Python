import unittest

#  Практическое задание к уроку № 2 (Циклы. Рекурсия. Функции.)

#  2. Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def even_odd(num: int) -> [int, int]:
    even = 0  # четное число
    odd = 0  # нечетное число
    while num > 0:
        if (num % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return even, odd


class test_even_odd(unittest.TestCase):
    def test_good_1(self):
        self.assertEqual((3, 3), even_odd(123456))
        self.assertEqual((0, 4), even_odd(1357))
        self.assertEqual((4, 0), even_odd(2468))
        self.assertEqual((2, 1), even_odd(100))

#  3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, то надо вывести число 6843.


def mirror_mum(num: int) -> int:
    mirror = 0  # перевернутое число
    while num > 0:
        mirror = mirror * 10 + num % 10
        num //= 10
    return mirror


class test_mirror_mum(unittest.TestCase):
    def test_good_2(self):
        self.assertEqual(654321, mirror_mum(123456))
        self.assertEqual(1, mirror_mum(1))
        self.assertEqual(0, mirror_mum(0))


def list_sum(num: int) -> int:
    x = 1
    sum_list = 1
    while num > 1:
        x = - x / 2
        sum_list += x
        num -= 1
    return sum_list


class test_list_sum(unittest.TestCase):
    def test_good_3(self):
        self.assertEqual(1, list_sum(1))
        self.assertEqual(0.75, list_sum(3))
        self.assertEqual(0.666015625, list_sum(10))


#  7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
#  выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def row_comparison(num: int) -> str:
    sum_num = 0
    for i in range(1, num + 1):
        sum_num += i
    equation = num * (num + 1) / 2
    if sum_num == equation:
        return 'yes'
    else:
        return 'yes'


class test_row_comparison(unittest.TestCase):
    def test_good_4(self):
        self.assertEqual('yes', row_comparison(1))
        self.assertEqual('yes', row_comparison(14654))
        self.assertEqual('yes', row_comparison(0))


# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count_num(user_range: str, user_like: str) -> int:
    count = 0
    for i in user_range:
        if i == user_like:
            count += 1
    return count


class test_count_num(unittest.TestCase):
    def test_good_5(self):
        self.assertEqual(0, count_num('12345', '6'))
        self.assertEqual(2, count_num('123451', '1'))
        self.assertEqual(5, count_num('11111', '1'))


# Дополнительное задание (344. Reverse String (from LeetCode))
# Перевернутая строка
# Напишите функцию, которая переворачивает строку. Входная строка задается как массив символов.
# С помощью рекурсии

def reverse_string(abc: str) -> str:
    if abc == "":
        return abc
    else:
        return reverse_string(abc[1:]) + abc[:1]


class test_reverse_string(unittest.TestCase):
    def test_good_6(self):
        self.assertEqual('0987654321', reverse_string('1234567890'))
        self.assertEqual('edcba', reverse_string('abcde'))
        self.assertEqual('mhtirogla', reverse_string('algorithm'))


# Дополнительное задание (231. Power of Two (from LeetCode))
# Подается целое число  'n', вернуть true, если оно является степенью двойки. В противном случае вернуть ложь.
# (Целое число  'n' является степенью двойки, если существует целое число x такое, что n == 2**x)
#   С помощью рекурсии:

def is_power_2(n: float) -> bool:
    if n == 1:
        return True
    elif 1 > n < 2:
        return False
    else:
        return is_power_2(n / 2)


class test_is_power_2(unittest.TestCase):
    def test_good_7(self):
        self.assertEqual(True, is_power_2(2))
        self.assertEqual(False, is_power_2(7))
        self.assertEqual(True, is_power_2(1024))
