class Solution:
    def findMin(self, nums: List[int]) -> int:

        right = len(nums) -1
        left = 0

        

        while right > left:
            middle = (right + left) //2

            print(nums[left:right])

            

            if nums[right] < nums[left] and nums[right] < nums[middle]:
                left = middle + 1
                print("left", nums[left])
            else:
                right = middle
                print("right:", nums[right], right)

        return nums[left]

            
            

        