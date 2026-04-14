class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start brute force
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            area = min(height[l],height[r]) * (r-l)
            if area > max_area: max_area = area

            if height[l] < height[r]:
                l+=1

            else: 
                r -= 1

        return max_area
            
