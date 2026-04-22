class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for i in strs:
            order = ''.join(sorted(i, key = str.lower))

            if order in dic:
                dic[order].append(i)
                
            else:
                dic[order] = [i]
        
        lis = []

        for key, value in dic.items():
            lis.append(value)

        return lis

    
        