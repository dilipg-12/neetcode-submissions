class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = dict()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell_value = board[i][j]
                
                if cell_value == ".":
                    continue
                    
                idx = (i // 3, j // 3)
                box_idx = boxes.setdefault(idx, set())
                
                if (cell_value in rows[i] or 
                    cell_value in cols[j] or 
                    cell_value in box_idx):
                    return False
                        
                rows[i].add(cell_value)
                cols[j].add(cell_value)
                box_idx.add(cell_value)
        return True


        