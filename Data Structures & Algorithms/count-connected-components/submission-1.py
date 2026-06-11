from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initially, every node is its own parent, and we have 'n' components
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        # 1. FIND function (with Path Compression)
        def find(node):
            res = node
            while res != parent[res]:
                # Path compression: make the node point to its grandparent
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        # 2. UNION function (with Union by Rank)
        def union(n1, n2):
            root1, root2 = find(n1), find(n2)

            # If they have the same root, they are already connected
            if root1 == root2:
                return 0

            # Merge the smaller graph into the larger graph
            if rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
                
            # Successfully merged two components into one
            return 1

        # 3. Process all edges
        for u, v in edges:
            components -= union(u, v)

        return components