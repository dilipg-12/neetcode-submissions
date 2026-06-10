class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        nodes = [[] for _ in range(n)]
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)
        q = deque([0])
        v = set()
        v.add(0)

        while q:
            node = q.popleft()
            for nei in nodes[node]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
        return len(v) == n
        