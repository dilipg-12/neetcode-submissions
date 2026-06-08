from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pac_queue = deque()
        atl_queue = deque()
        pac_reachable = set()
        atl_reachable = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 1. Setup Multi-Source queues for both oceans
        for c in range(cols):
            pac_queue.append((0, c)); pac_reachable.add((0, c))               # Top edge
            atl_queue.append((rows - 1, c)); atl_reachable.add((rows - 1, c)) # Bottom edge
            
        for r in range(rows):
            pac_queue.append((r, 0)); pac_reachable.add((r, 0))               # Left edge
            atl_queue.append((r, cols - 1)); atl_reachable.add((r, cols - 1)) # Right edge

        # 2. The BFS Explorer
        def bfs(queue, visited_set):
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check AND uphill check
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        (nr, nc) not in visited_set and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited_set.add((nr, nc))
                        queue.append((nr, nc))

        # 3. Trigger the massive simultaneous floods
        bfs(pac_queue, pac_reachable)
        bfs(atl_queue, atl_reachable)

        # 4. Find the intersection
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_reachable and (r, c) in atl_reachable:
                    result.append([r, c])
                    
        return result