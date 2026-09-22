class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:

            current_water = min(heights[l], heights[r]) * (r-l)

            if current_water > max_water:
                max_water = current_water
            
            if min(heights[l], heights[r]) == heights[l]:
                l +=1
            else:
                r -=1
        
        return max_water



        