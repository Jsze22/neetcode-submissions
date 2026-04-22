class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)

        for i in nums:

            dic[i] += 1
        

        lis = []

        for key, values in dic.items():

            lis.append((values, key))

        
        lis = sorted(lis, reverse = True)

        lis = lis[0:k]

        final = []

        for k, v in lis:
            final.append(v)

        return final
