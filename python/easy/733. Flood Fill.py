class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Solution: DFS and color each node visited that has the original color

        time: O(n)
        space: O(n)
        """
        original_color = image[sr][sc]
        def fill(x, y):
            if (
                x < len(image) and x >= 0 and 
                y < len(image[x]) and y >= 0 and 
                image[x][y] != color and 
                image[x][y] == original_color
            ):
                image[x][y] = color
                fill(x + 1, y)
                fill(x - 1, y)
                fill(x, y + 1)
                fill(x, y - 1)
        
        fill(sr, sc)
        return image
                