class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_start, n_start = 0, 0
        m_end, n_end = len(matrix)-1, len(matrix[0])-1

        

        while m_start <= m_end:
            if m_start < 0 or m_end >= len(matrix):
                return False

            mid_m = (m_start+m_end)//2
            if target < matrix[mid_m][0]:
                m_end = mid_m - 1
            elif target > matrix[mid_m][n_end]:
                m_start = mid_m + 1
            else:
                break

        while n_start <= n_end:
            mid_n = (n_start + n_end) //2
            if target > matrix[mid_m][mid_n]:
                n_start = mid_n +1
            elif target < matrix[mid_m][mid_n]:
                n_end = mid_n - 1
            else:
                return True
        return False
