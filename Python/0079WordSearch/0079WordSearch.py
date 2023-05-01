class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(m, n ,i ):
            if i == len(word):
                return True 

            if (m<0 or n<0 or m>=ROWS or n >=COLS or
                word[i] !=board[m][n] or
                ((m,n) in visited)):
                return False

            visited.add((m,n))
            
            res =  (dfs(m+1, n, i+1) or 
               dfs(m-1, n, i+1) or
               dfs(m, n+1, i+1) or
               dfs(m, n-1, i+1))

            visited.remove((m,n))
            return res

        for m in range(ROWS):
            for n in range(COLS):
                if dfs(m,n,0) == True:
                    return True

        return False
