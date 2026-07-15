class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left < right:

            middle = (left + right)//2

            if nums[right] < nums[middle]:
                if target <= nums[right] or target > nums[middle]:
                    left = middle +1
                else:
                    right = middle
            else:
                if target > nums[middle] and target <= nums[right]:
                    left = middle +1
                else:
                    right = middle

        if nums[left] == target:
            return left
        
        return -1