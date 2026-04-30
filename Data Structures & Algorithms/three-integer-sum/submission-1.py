class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        for i in range(len(nums) -1):
            here = set()

            for x in range(i + 1, len(nums)):
                triplet = tuple(sorted([nums[i], nums[x], (-nums[i]) + (-nums[x])]))

                if (-nums[i]) + (-nums[x]) in here:
                    seen.add(triplet)
                here.add(nums[x])
        
        return [list(t) for t in seen]

                
                


        