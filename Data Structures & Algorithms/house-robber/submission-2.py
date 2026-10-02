class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        if len(nums) ==2 :
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
        
        nums[2] += nums[0]
        biggest = nums[2] 

        for i in range(3, len(nums)):
            if nums[i-2]> nums[i-3]:
                nums[i] += nums[i-2]
            else:
                nums[i] += nums[i-3]
            print(i, nums[i])
            biggest = max(nums[i], biggest)

        return biggest


        