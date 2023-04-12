class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value != ".":
                    if value in rows[r]: return False
                    if value in cols[c]: return False
                    
                    square_R = r//3
                    square_C = c//3 
                    
                    if value in square[(square_R, square_C)]: return False

                    rows[r].add(value)
                    cols[c].add(value)
                    square[(square_R, square_C)].add(value)

        return True
