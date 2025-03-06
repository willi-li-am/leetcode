class Solution:
    def find(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "*":
                    return (i, j)
    def getFood(self, grid: List[List[str]]) -> int:
        """
        Simple BFS, first time reaching food is always shortest path
        """
        queue = deque()
        queue.append((self.find(grid), 0))

        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while(queue):
            values = queue.popleft()
            length = values[1]
            coord = values[0]
            x = coord[0]
            y = coord[1]

            if not (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])):
                continue

            if coord in visited:
                continue

            if grid[x][y] == "X":
                continue

            if grid[x][y] == "#":
                return length
            
            visited.add(coord)

            for d in directions:
                queue.append(((x + d[0], y + d[1]), length + 1))

        return -1