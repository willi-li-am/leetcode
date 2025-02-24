class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Idea: Using the fact that we can take courses [x, y, ... z], check if
        we can take all courses that require a prerequisite

        we go through each prerequisite of a course, if a prereq is is list then pass,
        else we check if that prereq is doable, if a cycle ever happens then return False

        time: O(n + m)
        space: O(n + m)
        """
        doable_list = [i for i in range(numCourses)]
        doable = set(doable_list)
        
        graph = {}
        # populate graph
        for prereq in prerequisites:
            need = prereq[1]
            course = prereq[0]
            
            if course in doable:
                doable.remove(course)

            if course in graph:
                graph[course].append(need)
            else:
                graph[course] = [need]

        visited = set()

        def dfs(num):
            if num in doable:
                return True
            if num in visited:
                return False

            visited.add(num)

            for prereq in graph[num]:
                if not dfs(prereq):
                    return False
            
            doable.add(num)
            return True

        for course in range(numCourses):
            if course in doable:
                continue
            
            visited = set()
            if not dfs(course):
                return False



        return True