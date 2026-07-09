class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = {}
        counter = 0
        longest = 0
        l = 0

        

        for i, c in enumerate(s):
            # print(unique)
            if c not in unique:
                unique[c] = i
                 
            else:
                # print(unique[c],"vs", i, "char", c, "left", l)
                if unique[c] >= l:
                    # print(s[0:i+1])
                    l = unique[c]+1
                    # print("current char", c, "left", l)
                    # print(i, "minus",l )
                    unique[c] = i
                    
                else:
                    unique[c] = i
            counter = i - l +1

            
            longest = max(longest, counter)
            # print(longest)

            
                
        return longest