class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        # my logic; not efficient enough
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(s_r, s_c):
            q = deque([(s_r, s_c, 0)])
            v = set()
            v.add((s_r, s_c))
            dist = 2147483647
            while q:
                r, c, n = q.popleft()
                for dr, dc in directions:
                    nt_r, nt_c = dr + r, dc + c
                    if (0 <= nt_r < rows and 0 <= nt_c < cols and grid[nt_r][nt_c] != -1 and (nt_r, nt_c) not in v):
                        if grid[nt_r][nt_c] == 0:
                            # print("pppp")
                            # print(nt_r, nt_c, n)
                            # print("5555")
                            dist = min(dist, n+1)
                        else:
                            v.add((nt_r, nt_c))
                            q.append((nt_r, nt_c, n+1 ))
            return dist

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)
        """
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        
        # 1. Multi-source start: queue all treasures (0s)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # 2. Flood outward
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nt_r, nt_c = dr + r, dc + c
                
                # We only care about bounds and unvisited rooms (INF)
                if (0 <= nt_r < rows and 
                    0 <= nt_c < cols and 
                    grid[nt_r][nt_c] == INF):
                    
                    # Overwrite INF. This acts as our "visited" marker!
                    grid[nt_r][nt_c] = grid[r][c] + 1
                    q.append((nt_r, nt_c))




