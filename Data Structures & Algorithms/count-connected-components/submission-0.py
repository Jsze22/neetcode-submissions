class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        graph = defaultdict(list)
        counter = 0

        for i in edges:
            x, y = i
            graph[x].append(y)
            graph[y].append(x)



        def find(val):
            if val in seen:
                return 
            seen.add(val)

            if val in graph:
                connection = graph[val]
                for x in connection:
                    find(x)
                seen.add(val)
            elif val not in graph:
                seen.add(val)

        
        for i in range(n):
            if i not in seen:
                find(i)
                counter+=1

        return counter



            

