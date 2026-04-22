class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        contain = {}

        for i in range(len(nums)):
            add = target - nums[i]
            if add in contain:
                return [contain[add], i]
            else:
                contain[nums[i]] = i
        return 