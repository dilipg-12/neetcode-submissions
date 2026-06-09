from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 1. Scan the borders. If we find an "O", mark it safe ("T") and queue it.
        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "T"
                q.append((r, 0))
            if board[r][cols - 1] == "O":
                board[r][cols - 1] = "T"
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "T"
                q.append((0, c))
            if board[rows - 1][c] == "O":
                board[rows - 1][c] = "T"
                q.append((rows - 1, c))

        # 2. BFS: Flood inward from the borders to find all connected safe zones
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nt_r, nt_c = r + dr, c + dc
                
                # If we step on an "O", it's connected to a border. Mark it safe!
                if 0 <= nt_r < rows and 0 <= nt_c < cols and board[nt_r][nt_c] == "O":
                    board[nt_r][nt_c] = "T"
                    q.append((nt_r, nt_c))

        # 3. Final Sweep: Flip everything to its correct final state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    # This "O" was never reached by the border BFS. It is surrounded.
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # This was a safe zone. Revert the temporary "T" back to "O".
                    board[r][c] = "O"