class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        required = len(need)
        have = 0 
        curr = {}
        left = 0
        shortest = float('inf')
        sub = ""

        if not s or not t:
            return ""

        for i, c in enumerate(s):    
            if c in need:
                curr[c] = curr.get(c, 0) + 1
                if curr[c] == need[c]:
                    have +=1

            while required == have:
                if i-left+1 < shortest:
                    shortest = i-left+1
                    sub = s[left: i+1]

                if s[left] in curr:
                    curr[s[left]] -=1
                    if curr[s[left]] < need[s[left]]:
                        have -=1
                left +=1
                
        return sub




