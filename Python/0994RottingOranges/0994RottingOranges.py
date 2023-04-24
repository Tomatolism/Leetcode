class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        total_fresh = 0
        step = 0 
        direction = [[0,1], [1,0], [0, -1], [-1, 0]]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    total_fresh +=1
                if grid[m][n] == 2:
                    q.append([m, n])

        while len(q) > 0 and total_fresh > 0:
            deque_len = len(q)

            for i in range(deque_len):
                cor = q.popleft()
                m, n = cor
                for dm, dn in direction:
                    new_m = m + dm
                    new_n = n + dn

                    if 0 <= new_m < len(grid) and 0 <= new_n < len(grid[0]):
                        if grid[new_m][new_n] == 1:
                            grid[new_m][new_n] = 2
                            q.append([new_m, new_n])
                            total_fresh -=1

            step +=1

        return step if total_fresh == 0 else -1
