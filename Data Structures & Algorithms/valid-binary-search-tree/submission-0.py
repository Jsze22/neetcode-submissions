# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:

            node, floor, ceiling = stack.pop()
            print(node.val)

            if node.left and node.val > node.left.val and node.left.val > floor:
                stack.append((node.left, floor, node.val ))
            if node.right and node.val < node.right.val and node.right.val < ceiling:
                stack.append((node.right, node.val, ceiling))
            
            if (node.left and (node.val <= node.left.val or node.left.val <= floor)) or (node.right and (node.val >= node.right.val or node.right.val >= ceiling)):
                return False

        return True

