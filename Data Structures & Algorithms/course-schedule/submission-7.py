class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        done = set()


        def helper(course):
            print("course", course)
            if course in visiting:
                print("here?")
                return False
            
            

            if course in done:
                return True
            
            visiting.add(course)

            for i in graph[course]:
                x = helper(i)

                if x == False:
                    return False

            visiting.remove(course)

            done.add(course)


            return True


        for course in range(numCourses):
            visiting = set()
            if course in done:
                continue
            if helper(course) == False:
                return False

        return True
        