class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l,r =0, r * c -1
        while l<=r:
            mid = (l +r)//2
            m = mid// c
            n = mid% c
            # if matrix[m][n] > target:
            if target > matrix[m][n]:
                l = mid + 1
            # elif matrix[m][n] < target:
            elif target <  matrix[m][n]:
                r = mid - 1
            else:
                return True
        return False
        