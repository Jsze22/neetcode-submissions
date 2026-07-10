class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        most = 0


        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            most = max(most, count[c])

            while i - most - left +1  > k:
                count[s[left]] -=1
                left +=1
            
            longest = max(longest, i-left+1)
            # if i - most - left <=k:
            #     longest = max(longest, i-left +1)
            # else:
            #     print("should not enter")
            #     count[s[left]] -=1
            #     left +=1
        
        return longest




            

        

        


