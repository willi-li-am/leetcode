class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        We loop through to find all initial X where we add to a queue, we only don't add to queue if it already has number
        BFS from each beginning Rotten orange until we visit each possible grids

        time: O(n * m)
        space: O(n * m) ... worst case since we can visit all elements of grid

        lowkey ass implementation, could be cleaner and also have less computations
        """

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        visited = set()
        while(queue):
            coords = queue.popleft()
            x = coords[0]
            y = coords[1]

            if not (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])):
                continue

            if (x, y) in visited:
                continue

            if grid[x][y] == 0:
                continue

            visited.add((x, y))

            # check all 4 sides and pick smallest
            smallest_side = 1000
            if x > 0 and grid[x - 1][y] >= 2:
                smallest_side = min(grid[x - 1][y], smallest_side)

            if x < len(grid) - 1 and grid[x + 1][y] >= 2:
                smallest_side = min(grid[x + 1][y], smallest_side)

            if y > 0 and grid[x][y - 1] >= 2:
                smallest_side = min(grid[x][y - 1], smallest_side)

            if y < len(grid[x]) - 1 and grid[x][y + 1] >= 2:
                smallest_side = min(grid[x][y + 1], smallest_side)

            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))
            
            # were guaranteed to have a smallest_side
            grid[x][y] = min(smallest_side + 1, grid[x][y]) if grid[x][y] != 1 else smallest_side + 1

        res = -1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
                res = max(res, grid[i][j])
        
        # case where all elements of grid are empty
        if res == 0:
            return 0

        return res - 2