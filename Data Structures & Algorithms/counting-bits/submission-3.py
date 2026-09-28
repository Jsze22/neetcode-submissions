class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0] * (n+1)


        for i in range(1, n+1):
            counter[i] = counter[i//2] + i%2 
  
        return counter