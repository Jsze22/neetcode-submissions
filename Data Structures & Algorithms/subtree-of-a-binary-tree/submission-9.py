# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = [root]
        sub_stack = [subRoot]
        compare = []
        same = True

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False


        while stack:
            node = stack.pop()

            if node is None:
                continue
            stack.append(node.right)
            stack.append(node.left)

            if node.val == subRoot.val:
                compare = [node]
                sub_stack = [subRoot]
                same = True

                while compare and sub_stack:

                    node = compare.pop()
                    node1 = sub_stack.pop()

                    if not node1 and not node:
                        continue
                    elif not node1 or not node:
                        same = False
                        break

                    if node.val != node1.val:
                        same = False
                        break
                    
                    compare.append(node.right)
                    compare.append(node.left)
                    sub_stack.append(node1.right)
                    sub_stack.append(node1.left)
                if same and not sub_stack and not compare:
                    return True
        return False

            

                



        



        