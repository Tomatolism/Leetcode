class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(1,0), (0,1), (-1,0), (0, -1)]
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        if color == start_color:
            return image

        def flip_color(i, j):
            image[i][j] = color
            for dir_i, dir_j in direction:
                next_i = i+dir_i
                next_j = j+dir_j
                if 0 <= next_i < m and 0 <= next_j < n :
                    if image[next_i][next_j] == start_color:
                        flip_color(next_i, next_j)

        flip_color(sr, sc)

        return image
