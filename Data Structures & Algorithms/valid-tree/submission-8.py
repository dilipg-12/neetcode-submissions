class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
A valid tree is defined by three rules:
        It is fully connected.
        It contains no cycles.
        It has exactly n - 1 edges.

        If a graph has exactly n - 1 edges, and it is fully connected, it is physically impossible for it to have a cycle. 
        Because of this property, you don't even need to track the origin or look for cycles at all!

        """
        if len(edges) != n -1:
            return False
        nodes = [[] for _ in range(n)]
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)
        q = deque([0])
        # v = set()
        # v.add(0)
        v = {0}
        while q:
            node = q.popleft()
            for nei in nodes[node]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
        return len(v) == n
        