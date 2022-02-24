import random

#  Практическое задание к уроку № 3 (Массивы. Кортежи. Множества. Списки.)

# 1. В диапазоне натуральных чисел от 2 до 99 определить,
#  сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(f'Для числа {n} кратны: {len(result[n])} чисел.\nКратные числа: {result[n]}\n')

# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# import random
r = [random.randint(0, 99) for _ in range(10)]  # создаем  массив мз случайных 10 чисел
print(f'Массив до изменения: {r}')

num_max = r[0]
num_min = r[0]

for i in r:
    if i > num_max:
        num_max = i
    elif i < num_min:
        num_min = i
min_index = r.index(num_min)
max_index = r.index(num_max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив после перестановки элементов {num_min} и {num_max}: {r}')


# 3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# import random

array = [random.randint(-9, 9) for _ in range(10)]
k = 0  # стартовый индекс массива
maximum = -10  # минимальное отрицательное число в массиве "array"
for i in range(len(array)):
    if array[i] < 0:
        if array[i] > maximum:
            maximum = array[i]
            k = i
print(f'Массив из случайных 10 чисел:\n{array}')
if maximum > -9:
    print(f'В массиве максимальный отрицательный элемент: {maximum}. '
          f'Находится в массиве на позиции {k + 1}')
else:
    print(f'В массиве нет отрицательных элементов')

# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

array = [random.randint(-9, 9) for _ in range(10)]

min_1 = array[0]
min_2 = array[1]

if min_1 > min_2:
    min_1, min_2 = min_2, min_1  # сортируем два первых элемента массива

for k in array[2:]:
    if k < min_1:
        min_1, min_2 = k, min_1  # меняем min_1 на меньшее значение (одновременно передаем прежний min_1 в min_2)
    elif k < min_2:
        min_2 = k  # вариант когда  k > min_1 ,  но k < min_2

print(f'Массив: {array}')
print(f'Сортированный массив: {sorted(array)}')  # для визуального удобства
print(f'Два наименьших элемента: {min_1} и {min_2}')


#  Доп задачи leetcode.com:

# 237. Удалить узел в связанном списке
# Напишите функцию для удаления узла в односвязном списке. Вам не будет предоставлен доступ к началу списка,
# вместо этого вам будет предоставлен доступ к удаляемому узлу напрямую.
# Гарантируется, что удаляемый узел не является хвостовым узлом в списке.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution237(object):
    def DeleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next




#  217 Учитывая целочисленный массив nums, вернуть true,
# если какое-либо значение встречается в массиве не менее двух раз, и вернуть false,
# если каждый элемент различен.

nums = [random.randint(1, 50) for _ in range(10)]  # случайный список
table = []  # список уникальных элементов


def contains_duplicate(n):
    for num in n:
        if num in table:  # если есть дубликат
            print(f'дубликат: {num}')
            return True
        else:
            table.append(num)  # формируемый список уникальных элементов
    return False  # если по заполнению table не оказалось дубликатов


print(sorted(nums))
print(contains_duplicate(nums))

