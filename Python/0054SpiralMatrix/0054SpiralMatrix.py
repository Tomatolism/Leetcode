class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        m, n = len(matrix), len(matrix[0])

        direction_list = ([0,1], [1,0], [0, -1], [-1, 0])
        direction = 0
        
        i, j = 0, 0
        VISIT = 111

        while len(res) < n*m:
            res.append(matrix[i][j])
            matrix[i][j] = VISIT

            if len(res) == n*m:
                break

            i_next = i + direction_list[direction][0] 
            j_next = j + direction_list[direction][1]

            while i_next>=m or j_next >= n or i_next <0 or j_next < 0 or matrix[i_next][j_next] ==VISIT:
                direction = (direction +1) % 4
                i_next = i + direction_list[direction][0] 
                j_next = j + direction_list[direction][1]

            i = i + direction_list[direction][0] 
            j = j + direction_list[direction][1]

        return res


