class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []

        for i in range(n +1):
            x = bin(i)
            x = x[2:]

            counter = 0



            for i in x:
                if i == str(1):
                    counter +=1

            count.append(counter)
        

        return count


        