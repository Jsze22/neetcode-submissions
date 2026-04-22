class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            temp = str(len(i))
            s = s + temp + '#' + i
        return s
        print(s)
    def decode(self, s: str) -> List[str]:

        lis = []
        
        i = 0

        temp = ""

        while i < len(s):
            
            if s[i] != '#':
                temp = temp + s[i]
                i +=1
            else:
                num = int(temp)
                temp = ""

                st = s[i+1:i+num+1]
                lis.append(st)
                i += num +1

        return lis





            
            

