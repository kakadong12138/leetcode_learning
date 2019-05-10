class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = len(set(s))+2
        for this_length in range(length,0,-1):
            for index in range(len(s) - this_length +1):
                new_s = s[index:this_length + index]
                
                if len(new_s) == len(set(new_s)):
                    return len(new_s)
                


s = Solution()
print(s.lengthOfLongestSubstring("aabaab!bb"))