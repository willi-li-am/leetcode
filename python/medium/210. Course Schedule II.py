class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Keep an array of all doable courses, as courses are discovered to be doable recursively add then to the list
        (The later a course is found to be doable, the later we should take that course)
        Since that course depends on the other courses

        time: O(n + m)
        space: O(n + m)
        """

        graph = [[] for i in range(numCourses)]

        for prereq in prerequisites:
            course = prereq[0]
            needs = prereq[1]

            graph[course].append(needs)

        res = []
        doable = set()
        for course in range(numCourses):
            if len(graph[course]) == 0:
                res.append(course)
                doable.add(course)

        def isDoable(course, visited):
            if course in doable:
                return True

            if course in visited:
                return False

            visited.add(course)

            for prereq in graph[course]:
                if not isDoable(prereq, visited):
                    return False
            
            res.append(course)
            doable.add(course)
            return True

        for course in range(numCourses):
            if not isDoable(course, set()):
                return []
        
        return res
            
