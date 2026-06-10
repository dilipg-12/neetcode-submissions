class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {i: [] for i in range(n)}
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)
        # q = deque([(edges[0][0], -1)])
        q = deque()
        v = set()
        print(f"{edges= }")
        q.append((0, -1))
        v.add(0)
        cycle =False
        print(q)
        # ... top of your code ...
        
        while q:
            curr, origin = q.popleft()  # FIX: Rename to 'curr'
            
            for nei in nodes[curr]:     # FIX: Use 'curr' here too
                if nei not in v:
                    q.append((nei, curr)) # FIX: Pass 'curr' as the new origin
                    v.add(nei)
                elif nei != origin:
                    cycle = True
                    
        return not cycle and len(v) == n


        