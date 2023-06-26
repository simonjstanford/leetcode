class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        L = 0
        R = len(height) -1
        
        max_area = 0
        while L < R:
            v1 = height[L]
            v2 = height[R]
            w = R-L
            area = w * min(v1, v2)
            max_area = max(max_area, area)
            if v1 < v2:
                L +=1
            else:
                R -=1
        
        return max_area
