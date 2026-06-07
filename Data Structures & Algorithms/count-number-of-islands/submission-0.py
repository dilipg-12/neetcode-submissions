class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        v = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0

        def bfs(r, c):
            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in directions:
                    nt_r, nt_c = dr + curr_r, dc + curr_c

                    if 0 <= nt_r < rows and 0 <= nt_c < cols and (nt_r, nt_c) not in v and grid[nt_r][nt_c] == "1":
                        v.add((nt_r, nt_c))
                        q.append((nt_r, nt_c))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in v:
                    if grid[r][c] == "1":
                        count += 1
                        v.add((r, c))
                        q.append((r, c))
                        bfs(r, c)
        return count