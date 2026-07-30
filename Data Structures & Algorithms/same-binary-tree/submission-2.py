# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p and not q) or (q and not p):
            return False

        if not p:
            return True

        if p.val != q.val:
            return False

        
        stack =[p]
        stack1= [q]

        while stack and stack1:

            node = stack.pop()
            node1 = stack1.pop()

            if node.right and node1.right and node.right.val != node1.right.val:
                print("right", node.right.val, node1.right.val)
                return False
            elif (node.right and not node1.right) or (node1.right and not node.right):
                print("here?")
                return False
            
            if node.left and node1.left and node.left.val != node1.left.val:
                print("left")
                return False
            elif (node.left and not node1.left) or (node1.left and not node.left):
                print("here?")
                return False
            

            if node.right:
                stack.append(node.right)
                stack1.append(node1.right)
            
            if node.left:
                stack.append(node.left)
                stack1.append(node1.left)


        return True