class Solution:
    def hammingWeight(self, n: int) -> int:

        counter =0

        while n >0:

            if n%2 >0:
                counter +=1

            n = n //2

        return counter