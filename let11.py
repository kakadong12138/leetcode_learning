def get_area(height,start_index,end_index):
    area = min(height[start_index] , height[end_index]) * (end_index - start_index)
    return area

class Solution:
    def maxArea(self, height):
        start_index = 0
        end_index = len(height)-1
        maxArea = 0
        while start_index < end_index:
            area = get_area(height,start_index,end_index)
            maxArea = max(maxArea,area)
            if height[start_index] < height[end_index]:
                start_index+=1
            else:
                end_index-=1
        return maxArea

s = Solution()
a = s.maxArea([1,3,1,6,2,5,4,8,3,7])
print(a)
