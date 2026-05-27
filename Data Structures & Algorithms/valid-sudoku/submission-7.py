class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols  = [set() for _ in range(len(board[0]))]
        boxes = dict()

        for i in range(len(board)):
            for j in range(len(board[0])):

                cell_value = board[i][j]

                if cell_value == ".":
                    continue

                if cell_value in rows[i] or cell_value in cols[j]:
                    return False

                rows[i].add(cell_value)
                cols[j].add(cell_value)

                box_idx = (i // 3, j // 3)

                if box_idx not in boxes:
                    boxes[box_idx] = set()

                if cell_value in boxes[box_idx]:
                    return False
                
                boxes[box_idx].add(cell_value)

        return True


        