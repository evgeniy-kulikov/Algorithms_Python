""" Задачи к урок 6.
Работа с динамической памятью """

# Параллельная обработка пакетов
# По данным n процессорам и m задач определите, для каждой из задач, каким процессором она будет обработана.
# https://stepik.org/course/1547/syllabus раздел 2.3 вторая задача


# выбор освободившегося процессора
def lift(i):
    min_index = i
    left, right = 2 * i + 1, 2 * i + 2
    if right <= size - 1 and arr[left] > arr[right] and arr[min_index] > arr[right]:
        arr[min_index], arr[right] = arr[right], arr[min_index]
        min_index = right
        lift(min_index)
    elif left <= size - 1 and arr[min_index] > arr[left]:
        arr[left], arr[min_index] = arr[min_index], arr[left]
        min_index = left
        lift(min_index)


n_processor = [int(i) for i in input().split()]
m_task = [int(i) for i in input().split()]
size = n_processor[0]
arr = [[0, i] for i in range(size)]
for i in m_task:
    print(arr[0][1], end=' ')
    print(arr[0][0])
    arr[0][0] = arr[0][0]+i
    lift(0)


# Доп задачи на деревья:
# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


class Solution:
    def connect(self, root):
        node = root
        while root:
            child_head = None
            child = None
            while root:
                if root.left:
                    if child_head is None:
                        child_head = root.left
                        child = root.left
                    else:
                        child.next = root.left
                        child = child.next
                if root.right:
                    if child_head is None:
                        child_head = root.right
                        child = root.right
                    else:
                        child.next = root.right
                        child = child.next
                root = root.next
            root = child_head
        return node
