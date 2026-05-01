class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) -1
        area =0

        while left < right:
            smaller = min(heights[left],heights[right])
            total = smaller * (right - left)
            if area < total:
                area = total
            
            if heights[left] < heights[right]:
                left +=1
            elif heights[right] < heights[left]:
                right -=1
            else:
                if heights[left +1] > heights[right-1]:
                    left +=1
                else:
                    right -=1

        return area