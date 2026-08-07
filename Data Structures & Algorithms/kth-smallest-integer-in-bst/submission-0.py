# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        if not root:
            return None

        stack = []
        temp = root

        while temp:
            stack.append(temp)
            temp = temp.left

        counter = 0

        while counter < k:

            node = stack.pop()
            counter +=1

            if counter == k:
                return node.val

            maybe = node.right

            while maybe:
                stack.append(maybe)
                maybe = maybe.left
