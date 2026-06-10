class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]* numCourses
        nodes = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            nodes[v].append(u)
            in_degree[u] += 1
        print(f"{in_degree= }")
        q = deque()
        result = []
        for n in range(numCourses):
            if in_degree[n] == 0:
                q.append(n)
                result.append(n)

        while q:
            new_node = q.popleft()
            for nei in nodes[new_node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
                    result.append(nei)
        return result if len(result) == numCourses else []
        



        