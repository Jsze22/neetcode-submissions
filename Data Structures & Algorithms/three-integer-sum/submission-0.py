class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final = []

        for i in range(len(nums) -1):
            here = set()

            for x in range(i + 1, len(nums)):
                triplet = sorted([nums[i], nums[x], (-nums[i]) + (-nums[x])])

                if (-nums[i]) + (-nums[x]) in here and triplet not in final:
                    final.append(triplet)
                here.add(nums[x])
        
        return final

                
                


        