class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = [[] for _ in range(len(nums) + 1)]
        dic = defaultdict(int)

        for i in nums:
            dic[i] +=1
        
        for key, v in dic.items():
            
            count[v].append(key)


        counter = 0
        final = []

        for i in reversed(count):

            for x in i:
                if counter < k:
                    final.append(x)
                    counter +=1
                    print(counter)
                else:
                    return final
                
        return final


                



        # dic = defaultdict(int)

        # for i in nums:

        #     dic[i] += 1
        

        # lis = []

        # for key, values in dic.items():

        #     lis.append((values, key))

        
        # lis = sorted(lis, reverse = True)

        # lis = lis[0:k]

        # final = []

        # for k, v in lis:
        #     final.append(v)

        # return final
