class Solution:
    def rob(self, nums: List[int]) -> int:
        cprev = 0
        fprev = 0

        for i in nums:
            current = max(cprev, fprev + i)
            fprev = cprev
            cprev = current
        
        return cprev



        