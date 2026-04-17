class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        a = {}
        b = {}
        for c, d in zip(s,t):
            a[c] = a.get(c, 0) + 1
            b[d] = b.get(d,0) +1
           
        
        return a == b
