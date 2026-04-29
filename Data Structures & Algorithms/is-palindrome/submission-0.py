class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = []
        
        for c in s:
            if c.isalnum():
                filtered.append(c)
        
        right = len(filtered) -1
        for i in range(len(filtered)):
            if filtered[i] != filtered[right -i]:
                return False
        
        return True
