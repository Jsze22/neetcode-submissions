class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best =0
        small = float('inf')

        for i in prices:

            small = min(i, small)
            best = max(best, i - small)
        
        return best