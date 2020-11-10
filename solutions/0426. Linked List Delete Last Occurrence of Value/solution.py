# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node, target):
        prev = curr = LLNode(None, node)
        target_node = None

        # traverse the linked list and keep the reference to last seen target
        while curr.next:
            if curr.next.val == target:
                target_node = curr
            curr = curr.next

        # finish traversing and delete the last occurrence of target
        if target_node:
            target_node.next = target_node.next.next

        return prev.next
