class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [ i for i in range(n+1)]
        # rank = [1 for i in range(n + 1)]
        rank = [1] * (n +1)

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(a, b):
            print("*" * 20)
            print(a, b)
            print(f"{rank=}")
            print(f"{parent=}")


            root_a, root_b = find(a), find(b)
            if root_a == root_b: return False
            if rank[root_b] > rank[root_a]:
                parent[root_a] = root_b
                rank[root_b] += rank[root_a]
            else:
                parent[root_b] = root_a
                rank[root_a] += rank[root_b]
            print("\n")
            print(f"{rank=}")
            print(f"{parent=}")
            print("-" * 20)
            
            return True

        for u,v in edges:
            if not union(u, v):
                return [u, v] 



