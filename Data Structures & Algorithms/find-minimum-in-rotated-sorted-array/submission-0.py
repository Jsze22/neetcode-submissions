class Solution:
    def findMin(self, nums: List[int]) -> int:

        right = len(nums) -1
        left = 0
        middle = 0
        small = float('inf')

        while right >=  left:
            middle = (right + left) //2

            if nums[right] < nums[left] and nums[right] < nums[middle]:
                small = min(nums[middle], small)
                left = middle + 1
            elif left == right:
                return min(nums[left], small)
            else:
                small = min(nums[middle], small)
                right = middle -1

        return small

            
            

        