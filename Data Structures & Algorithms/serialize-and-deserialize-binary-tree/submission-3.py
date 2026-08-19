# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = []

        if not root:
            return ""

        stack.append(root)
        word = ""
        
        while stack:
            node = stack.pop()

            if node == None:
                word += "N,"
            else:
                temp = str(node.val) + ","
                word += temp
                stack.append(node.right)
                stack.append(node.left)               

        return word
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None
        
        values = data.split(",")
        values = values[0:len(values)-1]
        i = 0


        def build():
            nonlocal i

            if values[i] == "N":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1

            node.left = build()
            node.right = build()

            return node

        return build()


            



