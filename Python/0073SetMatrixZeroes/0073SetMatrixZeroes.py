class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols, rows = len(matrix[0]), len(matrix) 

        First_row_zero = False

        # scan through matrix, and label the zero on the matrix
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        First_row_zero = True
                    else:  
                        matrix[r][0] = 0
                    

        # fill the value with 0 for certain line according to index line

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # deal with index line of col and rows

        if matrix[0][0] == 0:
            for r in range(1,rows):
                matrix[r][0] = 0

        if First_row_zero == True:
            for c in range(cols):
                matrix[0][c] = 0 

        return matrix
                    

