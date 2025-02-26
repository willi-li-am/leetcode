class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Solution: BFS starting at every 0

        time: O(n * m)
        space: O(n * m)
        """

        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    mat[i][j] = -1

        while(queue):
            coords = queue.popleft()
            x = coords[0]
            y = coords[1]
            num = coords[2]
            
            if mat[x][y] != -1 and num != 0:
                continue

            mat[x][y] = num
            
            if (x > 0):
                queue.append((x - 1, y, num + 1))

            if (x < len(mat) - 1):
                queue.append((x + 1, y, num + 1))

            if (y > 0):
                queue.append((x, y - 1, num + 1))

            if (y < len(mat[x]) - 1):
                queue.append((x, y + 1, num + 1))

        return mat
