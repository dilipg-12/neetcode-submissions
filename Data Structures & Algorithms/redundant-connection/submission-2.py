class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i:i for i in range(n+1)}
        rank = [1] * (n+1)
        
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(a,b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b: return 1
            
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a]
            return 0
        
        for u,v in edges:
            if union(u, v):
                return [u, v]
        