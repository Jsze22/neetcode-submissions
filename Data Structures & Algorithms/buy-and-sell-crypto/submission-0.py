class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best =0
        small = float('inf')

        for i in prices:

            if i < small:
                small = i
            else:
                if i - small > best:
                    best = i-small
        
        return best