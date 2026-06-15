class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        q = deque()

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

        while q:
            r, c = q.popleft()
            for dr, dc in direction:
                nt_r, nt_c = dr + r, dc + c
                if (0 <= nt_r < rows and
                    0 <= nt_c < cols and
                    board[nt_r][nt_c] == "O"):
                        board[nt_r][nt_c] = "T"
                        q.append((nt_r, nt_c))
                        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        # return board
        