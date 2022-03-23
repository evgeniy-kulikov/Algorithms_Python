"""
Задачи к уроку № 8 (Деревья. Хэш-функция)
"""

# 1319. Number of Operations to Make Network Connected (Количество операций для подключения к сети)
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


class Solution(object):
    """
    :type n: int
    :type connections: List[List[int]]
    :rtype: int
    """

    def makeConnected(self, n, connections):
        p = [x for x in range(n)]

        def union(x, y):
            p[find(x)] = find(y)

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        for x, y in connections:
            union(x, y)

        # соединение невозможно
        if len(connections) < n - 1:
            return -1

        # минимальное число возможных соединений
        count = 0
        for x in range(n):
            if x == find(x):
                count += 1
        return count - 1
