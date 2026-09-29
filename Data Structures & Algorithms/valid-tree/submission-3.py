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
            print(child)

            seen.add(child)

            for x in graph[child]:
                print(x, "loop")

                if x in seen and x != parent:
                    return False

                if x != parent:
                    print("enter", x)
                    dfs(child, x)
            return True


            

        seen.add(0)
        for x in graph[0]:
            truth = dfs(0, x)
            if not truth:
                return False

        for i in range(n):
            if i not in seen:
                return False
        return True

        


