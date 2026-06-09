from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list implementation, gemini logic
        in_degree = [0] * numCourses
        
        # Creates a list containing 'numCourses' empty lists
        nodes = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            nodes[v].append(u)
            in_degree[u] += 1

        q = deque()
        count = 0
        
        # FIX: Iterate using a standard index range
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
                count += 1

        while q:
            n = q.popleft()
            for nei in nodes[n]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
                    count += 1
                    
        return count == numCourses


