# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        if root is None:
            return 0
        if root.left and not root.right:
            return 1 + self.solve(root.left)
        if root.right and not root.left:
            return 1 + self.solve(root.right)
            
        return self.solve(root.right) + self.solve(root.left)
