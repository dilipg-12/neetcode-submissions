class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for u,v in prerequisites:
            node[v].append(u)
            in_degree[u] += 1
        q = deque()
        
        count = 0
        for i, v in enumerate(in_degree):
            if not v:
                q.append(i)
                count +=1
        while q:
            n = q.popleft()
            for nei in node[n]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    count += 1
                    q.append(nei)
        return count == numCourses
            