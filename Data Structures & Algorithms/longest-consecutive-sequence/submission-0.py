class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        find = set()
        longest = 0

        for i in nums:

            find.add(i)

            counter = 0
            a = i

            while a-1 in find:
                a -=1


            while a in find:
                counter +=1
                a+=1
            
            if counter > longest:
                longest = counter
            

        return longest


                
        