class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True
        seen = set()

        graph = {}
        
        for x in edges:
            l,r = x
            graph.setdefault(l, []).append(r)
            graph.setdefault(r, []).append(l)



        
        def dfs(parent, child):
            if child in seen:
                return False

            seen.add(child)

            for x in graph[child]:

                if x == parent:
                    continue

                if not dfs(child, x):
                    return False
            return True


            

        seen.add(0)
        for x in graph[0]:
            truth = dfs(0, x)
            if not truth:
                return False

        if len(seen) != n:
            return False
        return True

        


