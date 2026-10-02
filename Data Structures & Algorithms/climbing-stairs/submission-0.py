class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n


        ladder = [0] * (n+1)


        ladder[1] = 1
        ladder[2] = 2

        for i in range(3, len(ladder)):
            ladder[i] = ladder[i-1] + ladder[i-2]

        return ladder[-1]        

        