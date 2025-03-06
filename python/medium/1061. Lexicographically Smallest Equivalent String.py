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
        # the root of each character set is the smallest character in it's set
        x = self.find(x)
        y = self.find(y)

        # make the root of the set the smallest character
        if ord(x) > ord(y):
            self.graph[x] = y
        else:
            self.graph[y] = x

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        1. Unionize the characters with Union Find
        2. Key part is that we make the root of each character set is the smallest character
        3. We map through the baseStr to find the root of each character
        """
        union = UnionFind()

        for i in range(len(s1)):
            union.union(s1[i], s2[i])

        res = ""

        for x in baseStr:
            res += union.find(x)

        return res