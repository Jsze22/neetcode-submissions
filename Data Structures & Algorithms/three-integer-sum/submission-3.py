class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        seen = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1

            while left < right:
                ans = - nums[i]
                sums = nums[left] + nums[right]

                if ans > sums:
                    left +=1

                elif ans < sums:
                    right -=1
                else:
                    seen.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1

        return list(seen)
                
                
                


        