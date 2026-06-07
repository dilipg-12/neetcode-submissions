class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
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
            #         print(r, c)
            #         print(bfs(r, c))
            #         break
            # break





        # Input: [
        #         [2147483647,    -1,         0,          2147483647],
        #         [2147483647,    2147483647, 2147483647, -1],
        #         [2147483647,    -1,         2147483647, -1],
        #         [0,             -1,         2147483647, 2147483647]
        #         ]

        # Output: [
        # [3,-1,0,1],
        # [2,2,1,-1],
        # [1,-1,2,-1],
        # [0,-1,3,4]
        # ]