class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack is empty, width is 'i' (from 0 to i-1)
                # If not, width is (current_index - new_top - 1)
                width = i if not stack else i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        
        # Cleanup loop for bars that reached the end
        while stack:
            height = heights[stack.pop()]
            # These bars extend all the way to 'n'
            width = n if not stack else n - stack[-1] - 1
            ans = max(ans, height * width)
            
        return ans
        