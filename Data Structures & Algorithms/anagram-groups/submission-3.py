class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for i in strs:
            order = ''.join(sorted(i))

            dic[order].append(i)
        
        return list(dic.values())

    
        