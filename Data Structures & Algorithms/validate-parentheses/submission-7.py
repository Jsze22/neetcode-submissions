class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i != dic[stack.pop()]:
                    return False
                

        if stack:
            return False
        
        return True

