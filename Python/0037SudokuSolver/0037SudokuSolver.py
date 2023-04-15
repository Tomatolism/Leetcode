class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validBoard(i, j, value):
            value = str(value)
            for m in range(9):
                if board[i][m] == value:
                    return False
                if board[m][j] == value:
                    return False
            square_i, square_j = i//3*3, j//3*3 
            for m in range(3):
                for n in range(3):
                    if board[square_i+m][square_j+n] == value:
                        return False
            return True

        def dfs(i, j):
            if i == 9: return True
            if j == 9: return dfs(i+1, 0)
            if board[i][j] != '.': 
                return dfs(i, j+1)

            for value in range(1, 10):
                if validBoard(i, j, value):
                    board[i][j] = str(value)
                    if dfs(i, j+1)==True:
                        return True

            board[i][j] = '.'


        dfs(0,0)
        return board
