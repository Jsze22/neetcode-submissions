# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr = [root]
        deep = []
        total =[]
        value= []

        if root == None:
            return []

        while curr:
            
            for i in curr:

                value.append(i.val)

                if i.left:
                    deep.append(i.left)
                if i.right:
                    deep.append(i.right)
                
            total.append(value)
            value = []
            curr = deep
            deep =[]


        return total
            




            