class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course):

            if visited[course] == 2:
                return False
            if visited[course] == 1:
                return True
            
            visited[course] = 2

            for nextCourse in relation[course]:
                if not dfs(nextCourse):
                    return False
            visited[course] =1

            return True

        visited = [0]* numCourses
        relation = collections.defaultdict(list)

        for after, before in prerequisites:
            relation[before].append(after)

        for i in range(numCourses):
            if visited[i] == 0: ## This line is critical to improve access speed.
                if not dfs(i):
                    return False

        return True
            
