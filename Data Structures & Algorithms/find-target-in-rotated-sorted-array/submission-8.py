class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left < right:

            middle = (left + right)//2

            if nums[right] < nums[middle]:
                print("1")
                if target <= nums[right] or target > nums[middle]:
                    left = middle +1
                else:
                    right = middle
            else:

                print("2")
                if target > nums[middle] and target <= nums[right]:
                    left = middle +1
                else:
                    print("second")
                    right = middle
                    print("right", nums[right])



        if nums[left] == target:
            return left
        
        return -1