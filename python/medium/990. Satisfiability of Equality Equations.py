class UnionFind:
    def __init__(self):
        self.graph = {}

    def find(self, x):
        if x not in self.graph:
            self.graph[x] = x
        if x != self.graph[x]:
            self.graph[x] = self.find(self.graph[x])
        
        return self.graph[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        self.graph[x] = y

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        1. We unionize the equations with Union Find
        2. We check each inequality to see if they are any contradictions
        """
        ineq = []
        union = UnionFind()
        for eq in equations:
            if eq[1] == "=":
                union.union(eq[0], eq[3])
            else:
                ineq.append(eq)

        for eq in ineq:
            if union.find(eq[0]) == union.find(eq[3]):
                return False
        
        return True