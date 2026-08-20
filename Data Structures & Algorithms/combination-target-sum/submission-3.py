class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combos = []



        def helper(start, current, combo):

            if current == target:
                combos.append(combo.copy())
                return
            
            for i in range(start, len(nums)):
                if current + nums[i]> target:
                    continue
                else:
                    combo.append(nums[i])
                    helper(i, current + nums[i], combo)
                    combo.pop()

        
        helper(0, 0, [])

        return combos

            
                
                

        