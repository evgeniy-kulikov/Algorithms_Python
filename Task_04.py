#  155. Min Stack
#  https://leetcode.com/problems/min-stack/
#  Разработайте стек, который поддерживает push, pop, top и извлечение минимального элемента за постоянное время.

class MinStack:
    def __init__(self):
        # создаем стек в виде пустого списка
        self.stack = []

    def push(self, val):
        if not self.stack:  # если стек пустой, то положенный элемент и минимальный равны
            self.stack.append((val, val))
        else:
            #  иначе добавляем в стек значения из верхушки (последнего элемента)
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self):
        # просто удаляем элемент
        self.stack.pop()

    def top(self):
        # получаем значение из верхушки элемента
        return self.stack[-1][0]

    def getMin(self):
        # получаем значение минимума из верхушки элемента
        return self.stack[-1][1]


#  Симуляция обработки сетевых пакетов (Реализовать обработчик сетевых пакетов)
#  https://stepik.org/lesson/41234/step/3?unit=19818

#  Размер буфера size и число пакетов n
size, n = map(int, input().split())

packages = []  # список для n пакетов, состоящий из элементов [arrival, duration]
time = 0
buffer = []  # Список, который содержит время окончания обработки пакетов, которые сейчас находятся в буфере

# Заполняем список из n пакетов элементами [arrival, duration]:
for i in range(n):
    arrival, duration = map(int, input().split())
    packages.append([arrival, duration])

if n != 0:
    for package in packages:
        if len(buffer) == 0:  # Если буфер пустой,
            # то пакет - первый в очереди на обработку (записываем время окончания обработки пакета)
            buffer.append((package[0] + package[1]))
            package.append(package[0])  # и время начала обработки = времени поступления пакета
        else:
            # Перед рассмотрением каждого нового пакета очищаем буфер
            # (удаляем элементы, которые к этому моменту уже должны были выполниться)
            while buffer[0] <= package[0] and len(buffer) > 1:
                buffer.pop(0)

            # Если буфер в процессе очистки сократился до одного элемента и этот последний элемент тоже уже должен был
            # выполниться, то этот последний элемент обрабатываем отдельно
            if buffer[0] <= package[0]:
                buffer[0] = package[0] + package[1]
                package.append(package[0])
            # В остальных случаях:
            else:
                if len(buffer) < size:  # Если после проверки буфера, в нём остались элементы, но есть место для новых:
                    # то добавляем пакет (точнее время его выполнения) в конец буфера
                    buffer.append(buffer[-1] + package[1])
                    # в пакет записываем время начала его исполнения, равное времени завершения предыдущего пакета
                    package.append(buffer[-2])
                else:
                    package.append(-1)  # Если места в буфере нет, то пакет "отбрасывается"
    # Распечатка ответа:
    for package in packages:
        print(package[2])
