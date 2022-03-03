#  101. Symmetric Tree
#  Проверить дерево на симметричность
#  https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        def helper(left, right):  # одновременная проверка части левой и правой ветки
            if not left and not right:  # окончания веток совпадают - есть симметрия
                return True
            if not left or not right:  # иначе - симметрии нет
                return False
            # проверка на одинаковость значений и зеркальность веток
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root, root)



#  145. Binary Tree Postorder Traversal
#  Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень:
#  https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        def post(root, result):
            if root is None:  # если корень пустой
                return None
            post(root.left, result)
            post(root.right, result)
            result.append(root.val)
        result = []  # формируемый обратный порядок значений  узлов
        post(root, result)
        return result



