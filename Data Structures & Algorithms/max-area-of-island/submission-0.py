class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        v = set()
        result = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            v.add((start_r, start_c))
            area = 0

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nt_r, nt_c = dr + r, dc + c
                    if (0 <= nt_r < rows and 0 <= nt_c < cols and grid[nt_r][nt_c] == 1 and (nt_r, nt_c) not in v):
                        area += 1
                        q.append((nt_r, nt_c))
                        v.add((nt_r, nt_c))
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in v:
                    result = max(result, 1 + bfs(r, c))
        return result
        