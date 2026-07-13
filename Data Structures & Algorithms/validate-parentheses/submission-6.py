class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in dic:
                stack.append(i)
                print('here')
            else:
                print('no')
                if not stack:
                    return False
                if i != dic[stack.pop()]:
                    return False
                

        if stack:
            return False

        print("what")
        
        return True

