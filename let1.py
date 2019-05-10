class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for i2,num2 in enumerate(nums[i+1:]):
                if num+num2 == target:
                    return [i,i2+i+1]
                
s = Solution()
r = s.twoSum([2,7,11,15],9)
print(r)