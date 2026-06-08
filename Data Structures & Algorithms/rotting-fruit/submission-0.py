class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh:
            time +=1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nt_r, nt_c = dr + r, dc + c
                    if ( 0 <= nt_r < rows and
                    0 <= nt_c < cols and
                    grid[nt_r][nt_c] == 1):
                        q.append((nt_r, nt_c))
                        grid[nt_r][nt_c] = 2
                        fresh -= 1

        return time if not fresh else -1


        

        

        