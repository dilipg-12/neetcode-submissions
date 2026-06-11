class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for i in range(n)]
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        q = deque()
        v = set()
        count = 0

        for i in range(n):
            if i not in v:
                count += 1
                q.append(i)
                v.add(i)

                while q:
                    node = q.popleft()
                    for nei in nodes[node]:
                        if nei not in v:
                            q.append(nei)
                            v.add(nei)
        return count

        