class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for i in strs:
            order = ''.join(sorted(i))

            if order in dic:
                dic[order].append(i)
                
            else:
                dic[order] = [i]
        
        return list(dic.values())

    
        