class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        direction = [[1,0], [-1, 0], [0,1], [0, -1]]
        distance = 1

        for m in range(len(mat)):
            for n in range(len(mat[0])):
                
                if mat[m][n] == 1: # chang value 1 to infinity
                    mat[m][n] = float('inf')
                else:
                    q.append([m,n])

        while q:
            q_len = len(q)
            for i in range(q_len):
                m, n = q.popleft()
                for dm, dn in direction:
                    new_m, new_n = m+dm, n+dn
                    if 0 <= new_m < len(mat) and 0 <= new_n <len(mat[0]):
                        if mat[new_m][new_n] > distance:
                            mat[new_m][new_n] = int(distance)
                            q.append([new_m,new_n])
            
            distance +=1

        return mat
