"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        dic = {}

        def helper(curr_n):

            if curr_n in dic:
                return dic[curr_n]
            
            if curr_n == None:
                return

            dic[curr_n] = Node(curr_n.val)

            for neighbor in curr_n.neighbors:
                cloned = helper(neighbor)
                dic[curr_n].neighbors.append(cloned)

            return dic[curr_n]


        return helper(node)

        

            
        

        
        

        