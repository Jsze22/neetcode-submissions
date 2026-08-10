class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result =[]

        


        def back (start, remaining, current):

            if remaining ==0:
                result.append(current.copy())
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                back(i, remaining - nums[i], current)
                current.pop()

        back(0, target, [])

        return result

                 


        