class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2: return False
        stack = []
        open = "({["
        map = {'}':'{', ')':'(', ']':'['}
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if len(stack) and stack[-1] == map[char]:
                    stack.pop()
                else: 
                    return False
        return False if stack else True
    


print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False
print(Solution().isValid("([)]")) # False
print(Solution().isValid("[()[{(}]()]")) # False
print(Solution().isValid("]]]")) # False