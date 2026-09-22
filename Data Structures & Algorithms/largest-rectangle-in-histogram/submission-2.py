class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for ind, h in enumerate(heights):
            start = ind
            while stack and h < stack[-1][1]:
                i, h_cur = stack.pop()
                max_area = max(max_area, h_cur * (ind - i))
                start = i
            
            stack.append((start,h))
        
        for ind, h in stack:
            max_area = max(max_area, h * (len(heights) - ind))

        return max_area