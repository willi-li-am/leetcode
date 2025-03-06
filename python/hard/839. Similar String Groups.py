class UnionFind:
    def __init__(self):
        self.graph = {}

    def find(self, x):
        if x not in self.graph:
            self.graph[x] = x
        elif x != self.graph[x]:
            self.graph[x] = self.find(self.graph[x])
        
        return self.graph[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        self.graph[x] = y



class Solution:
    def is_similar(self, x, y):
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
            if count > 2:
                return False
        
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        """
        Union Find where we check if any two already seen string is similar
        Then we loop through every string and check how many different roots
        """
        union = UnionFind()

        for x in strs:
            visited = union.graph.copy()
            for y in visited:
                if self.is_similar(x, y):
                    union.union(x, y)
            
            union.find(x)
        res = 0
        visited = set()
        for x in strs:
            x = union.find(x)
            if x not in visited:
                res += 1
            visited.add(x)

        return res