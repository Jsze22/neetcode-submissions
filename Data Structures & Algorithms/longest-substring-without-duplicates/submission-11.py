class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = {}
        counter = 0
        longest = 0
        l = 0

        

        for i, c in enumerate(s):
            if c in unique and unique[c] >= l:
                l = unique[c]+1
            
            unique[c] = i
            
            longest = max(longest, i-l+1)

            
                
        return longest