import unittest

#  Практическое задание к уроку № 1 (Введение в алгоритмизацию)
#
#  1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_multiply(a: int) -> [int, int]:
    num_sum, num_mult = 0, 1
    while a > 0:
        num_sum += a % 10
        num_mult *= a % 10
        a = a // 10
    return num_sum, num_mult

# другое решение (на три переменных больше)
# def sum_multiply(a: int) -> [int, int]:
#     num_1 = a // 100
#     num_2 = (a % 100) // 10
#     num_3 = a % 10
#     num_sum = num_1 + num_2 + num_3
#     num_mult = num_1 * num_2 * num_3
#     return num_sum, num_mult


class test_sum_multiply(unittest.TestCase):
    def test_good_1(self):
        self.assertEqual((15, 120), sum_multiply(456))
        self.assertEqual((9, 0), sum_multiply(900))
        self.assertEqual((7, 0), sum_multiply(205))


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
#    и сколько между ними находится букв.

def two_letter(letter_1: str, letter_2: str) -> [int, int, int]:
    letter_1 = ord(letter_1.lower())
    letter_2 = ord(letter_2.lower())
    pos_letter_1 = letter_1 - ord('a') + 1
    pos_letter_2 = letter_2 - ord('a') + 1
    dist_letter = abs(letter_1 - letter_2) - 1
    return pos_letter_1, pos_letter_2, dist_letter


class test_two_letter(unittest.TestCase):
    def test_good_2(self):
        self.assertEqual((1, 26, 24), two_letter('A', 'Z'))
        self.assertEqual((26, 1, 24), two_letter('z', 'a'))
        self.assertEqual((1, 2, 0), two_letter('a', 'b'))
        self.assertEqual((1, 1, -1), two_letter('a', 'a'))


#  8. Определить, является ли год, который ввел пользователем, високосным или не високосным.

def even_year(year: int) -> str:
    if year % 400 == 0:
        answer = 'високосный'
    elif year % 100 == 0 and year % 400 != 0:
        answer = 'невисокосный'
    elif year % 4 == 0:
        answer = 'високосный'
    else:
        answer = 'невисокосный'
    return answer


class test_even_year(unittest.TestCase):
    def test_good_3(self):
        self.assertEqual('високосный', even_year(2000))
        self.assertEqual('високосный', even_year(2004))
        self.assertEqual('невисокосный', even_year(1900))
        self.assertEqual('невисокосный', even_year(2021))



# Дополнительное задание № 1
# Удалить дубликаты из отсортированного массива
# Имеется целочисленный массив nums, отсортированный в неубывающем порядке,
# удалите дубликаты на месте, чтобы каждый уникальный элемент появлялся только один раз.
# Относительный порядок элементов должен быть сохранен.

def removeDuplicates(in_list: list, n: int) -> [list, int]:
    # создаем временный спмсок одинакового размера с исходным
    temp_list = list(range(n))
    j = 0  # счетчик уникальных элементов
    for i in range(0, n - 1):
        # если текущий элемент не равен следующему, то помещаем его в новый список
        if in_list[i] != in_list[i + 1]:
            temp_list[j] = in_list[i]
            j += 1
    temp_list[j] = in_list[n - 1]  # фиксируем последний сохраненный элемент
    j += 1
    # создание требуемого списка (заполняем начало уникальными элементами. Хвост остается исходным)
    for i in range(0, j):
        in_list[i] = temp_list[i]
    return j, in_list

class test_removeDuplicates(unittest.TestCase):
    def test_good_4(self):
        self.assertEqual((7, [1, 2, 4, 5, 6, 7, 99, 6, 7, 99]), removeDuplicates([1, 2, 2, 4, 4, 5, 5, 6, 7, 99], 10))
        self.assertEqual((1, [1]), removeDuplicates([1], 1))
        self.assertEqual((1, [2, 2, 2, 2, 2]), removeDuplicates([2, 2, 2, 2, 2], 5))
        self.assertEqual((1, [0, 0, 0]), removeDuplicates([0, 0, 0], 3))


#  Дополнительное задание № 2
#  В целочисленном массиве переместить все 0 (нули) в его конец, сохраняя относительный порядок ненулевых элементов.

def moveZeroes(arr: list, n: int) -> list:
    count = 0  # счетчик элементов != 0
    for i in range(n):  # подчитываем кол-во элементов != 0
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:  # заполняем оставшуюся часть списка нулями
        arr[count] = 0
        count += 1
    return arr

class test_moveZeroes(unittest.TestCase):
    def test_good_4(self):
        self.assertEqual(([1, 6, 4, 7, 6, 8, 0, 0, 0, 0]), moveZeroes([1, 6, 4, 0, 0, 7, 0, 6, 0, 8], 10))
        self.assertEqual(([1, 0]), moveZeroes([0, 1], 2))
        self.assertEqual(([0, 0, 0]), moveZeroes([0, 0, 0], 3))
        self.assertEqual(([3, 2, 1]), moveZeroes([3, 2, 1], 3))
