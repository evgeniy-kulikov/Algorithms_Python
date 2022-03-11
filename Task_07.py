""" Задачи к урок 7.
 Алгоритмы сортировки """


"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой —
не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка
слиянием также недопустима).
"""
from random import randint


def median_find(arr):
    pivot = arr[0]
    less_median = []  # писок элементов < медианы
    greater_median = []  # писок элементов > медианы
    left_median_shoulder = 0
    right_median_shoulder = 0

    # считаем за один прогон и плечи медианы и вычисляем диапазон поиска новой медианы
    for i in array:
        if i < pivot:
            left_median_shoulder += 1
        elif i > pivot:
            right_median_shoulder += 1

        if i in arr:
            if i < pivot:
                less_median.append(i)
            elif i > pivot:
                greater_median.append(i)

    if left_median_shoulder > right_median_shoulder:
        return median_find(less_median)
    elif left_median_shoulder < right_median_shoulder:
        return median_find(greater_median)

    return pivot


# n = int(input("Введите положительное целое: "))
n = 6
# Количество элементов массива (нечетное)
m = 2 * n + 1

# создание массива из неповторяющихся элементов
max_val = pow(m, 2)
array = []
while len(array) < m:
    x = randint(0, max_val)
    if x not in array:
        array.append(x)

print(f"Для массива {array}\nмедиана равна: {median_find(array)}")

""" 
задачи на префиксное дерево
https://leetcode.com/problems/replace-words/
648. Replace Words
"""


class Solution(object):

    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        set_dict = set(dictionary)
        sentence_in_list = sentence.split(" ")
        return_list = [self.find_root(word, set_dict) for word in sentence_in_list]

        return " ".join(return_list)

    def find_root(self, word, dict_set):
        for head in range(1, len(word)):
            if word[:head] in dict_set:
                return word[:head]
        return word


