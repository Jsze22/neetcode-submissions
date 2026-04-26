class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        find = set()
        longest = 0
        
        for i in nums:
            find.add(i)
        
        for x in find:
            a = x
            counter = 0
            while a-1 in find:
                a-=1
            
            while a in find:
                print(a)
                a +=1
                counter +=1
            if counter > longest:
                longest = counter
        
        return longest


                
        