class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i=0
        j = len(heights)-1
        #for i in range(0,len(nums-1)):
        while(i<j and i<len(heights)-1 and j > 0):
            area = (j-i)*min(heights[i],heights[j])
            if area > maxArea:
                maxArea = area
            if heights[i] < heights[j]:
                i = i+1
            else:
                j=j-1
        return maxArea
